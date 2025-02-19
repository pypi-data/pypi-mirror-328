import logging

import jax.numpy as jnp
import lal
import lalpulsar
import numpy as np
from pyfstat import DetectorStates
from pyfstat.utils import get_sft_as_arrays

logger = logging.getLogger(__name__)


class SFTDataIO:
    def __init__(
        self,
        sftfilepath: str,
        freq_min: float = -1,
        freq_max: float = -1,
        running_median_window: int = lalpulsar.FstatOptionalArgsDefaults.runningMedianWindow,
    ):
        """
        sftfilepath:
            Path to SFT data file(s).
        freq_min:
            Minimum SFT frequency to load. `-1` means the lowest frequency
            present on the file.
        freq_max:
            Minimum SFT frequency to load. `-1` means the highest frequency
            present on the file.
        running_median_window:
            Number of bins to compute a running median. Defaults to lalpulsar's default.
            Basically don't touch it unless you know what you are doing.
        """
        self.sftfilepath = sftfilepath
        self.freq_min = freq_min
        self.freq_max = freq_max
        self.running_median_window = running_median_window

        self._get_data_from_sfts()

    def __call__(self, sky_position: tuple[float, float] | None = None):
        """
        Returns SFT power, timestamps, velocities, and weights
        for a given sky position so that JAX can operate on them.

        Weights are normalized so that `weights.sum() == 1`.

        Parameters
        -------------
        sky_position:
            Tuple containing (right_ascension, declination) in radians.

        Returns
        ---------
        tuple[power, timestamps, velocities, weights, t_sft, bin_0]
        """
        power = jnp.hstack([val["power"] for val in self.multisft_data.values()])
        timestamps = jnp.hstack(
            [val["timestamps"] for val in self.multisft_data.values()]
        )
        velocities = jnp.hstack(
            [val["velocities"] for val in self.multisft_data.values()]
        )

        weights = self.get_weights(sky_position)
        weights = weights / weights.sum()

        return (
            power,
            timestamps,
            velocities,
            weights,
            jnp.array(
                [
                    self.common_data["t_sft"],
                ]
            ),
            jnp.array([self.common_data["bin_0"]]),
        )

    def get_weights(self, sky_position=None):
        weights = self.get_noise_weights()
        if sky_position is not None:
            a, b = self.get_a_b(sky_position)
            weights = (a**2 + b**2) * weights
        return weights

    def get_noise_weights(self):
        return jnp.hstack([val["noise_weights"] for val in self.multisft_data.values()])

    def get_a_b(self, sky_position):
        AMcoeffs = self._get_AMcoeffs(*sky_position)
        a = jnp.hstack([val.a.data for val in AMcoeffs.values()])
        b = jnp.hstack([val.b.data for val in AMcoeffs.values()])
        return a, b

    def _get_data_from_sfts(self):
        """
        Uses PyFstat's get_sfts_as_arrays function to get the SFT's
        frequencies, timestamps, power, and noise weights.
        """
        logger.info(f"Parsing SFT catalog from {self.sftfilepath}...")
        sft_catalog = lalpulsar.SFTdataFind(self.sftfilepath, None)

        ifo_labels = lalpulsar.ListIFOsInCatalog(sft_catalog)

        logger.info(f"Reading SFTs from {self.freq_min} Hz to {self.freq_max} Hz...")
        multi_sfts = lalpulsar.LoadMultiSFTs(
            sft_catalog,
            fMin=self.freq_min,
            fMax=self.freq_max,
        )
        assert multi_sfts.length == ifo_labels.length

        logger.info(f"Normalizing SFTs and computing noise weights...")
        rngmed = lalpulsar.NormalizeMultiSFTVect(
            multsft=multi_sfts,
            blockSize=self.running_median_window,
            assumeSqrtSX=None,
        )
        multi_noise_weights = lalpulsar.ComputeMultiNoiseWeights(
            rngmed, self.running_median_window, 0
        )
        assert multi_noise_weights.length == multi_sfts.length
        assert not multi_noise_weights.isNotNormalized

        multidetector_states = DetectorStates().get_multi_detector_states_from_sfts(
            self.sftfilepath,
            central_frequency=0.5 * (self.freq_min + self.freq_max),
            time_offset=0.5 / multi_sfts.data[0].data[0].deltaF,
        )
        assert multidetector_states.length == ifo_labels.length

        for ifo_ind in range(ifo_labels.length):
            assert (
                multi_sfts.data[ifo_ind].length
                == multi_noise_weights.data[ifo_ind].length
            )
            assert (
                multi_sfts.data[ifo_ind].length
                == multidetector_states.data[ifo_ind].length
            )

        self.multisft_data = {}
        for ifo_ind, ifo_name in enumerate(ifo_labels.data):
            logging.debug(f"Reading data from IFO {ifo_name}")

            sfts = multi_sfts.data[ifo_ind]
            sft_amplitude = np.array([sft.data.data for sft in sfts.data]).T
            f0 = sfts.data[0].f0
            df = sfts.data[0].deltaF

            sft_data = {}
            sft_data["timestamps"] = np.array(
                [sft.epoch.gpsSeconds for sft in sfts.data]
            )
            sft_data["power"] = 2.0 * (
                sft_amplitude.real**2 + sft_amplitude.imag**2
            )
            sft_data["noise_weights"] = multi_noise_weights.data[ifo_ind].data

            nbins, nsfts = sft_data["power"].shape

            sft_data["frequency_Hz"] = np.linspace(f0, f0 + (nbins - 1) * df, nbins)
            sft_data["t_sft"] = int(
                1 / (sft_data["frequency_Hz"][1] - sft_data["frequency_Hz"][0]) + 0.5
            )
            sft_data["bin_0"] = int(
                sft_data["t_sft"] * sft_data["frequency_Hz"][0] + 0.5
            )

            sft_data["states"] = multidetector_states.data[ifo_ind]
            sft_data["velocities"] = np.vstack(
                [data.vDetector for data in multidetector_states.data[ifo_ind].data]
            ).T

            self.multisft_data[ifo_name] = sft_data

        self.common_data = {}
        for common_key in ["t_sft", "bin_0"]:
            common_value = list(
                set([ifo_data[common_key] for ifo_data in self.multisft_data.values()])
            )
            assert len(common_value) == 1
            self.common_data[common_key] = common_value[0]

    def _get_AMcoeffs(self, right_ascension: float, declination: float):
        logging.debug(
            f"Computing antenna pattern functions at ({right_ascension}, {declination})"
        )
        skypos = lal.SkyPosition()
        skypos.longitude = right_ascension
        skypos.latitude = declination
        skypos.system = lal.COORDINATESYSTEM_EQUATORIAL
        lal.NormalizeSkyPosition(skypos.longitude, skypos.latitude)

        AMcoeffs = {}
        for ifo_ind, ifo_label in enumerate(self.multisft_data):
            AMcoeffs[ifo_label] = lalpulsar.ComputeAMCoeffs(
                DetectorStates=self.multisft_data[ifo_label]["states"],
                skypos=skypos,
            )
        return AMcoeffs
