import os
from shutil import rmtree
import sys

import pytest

import pyfstat
from fasttracks.dataio import SFTDataIO

@pytest.fixture
def writer_kwargs(tmp_path):
    return {
        "label": "anInjection",
        "outdir": tmp_path / "SampleData",
        "tstart": 1238166018,
        "duration": 10 * 86400,
        "detectors": "H1,L1",
        "sqrtSX": 1e-23,
        "Tsft": 1800,
        "SFTWindowType": "tukey",
        "SFTWindowParam": 0.01,
        "Band": 0.2,
    }

@pytest.fixture
def signal_parameters(writer_kwargs):
    return {
        "F0": 100.0,
        "F1": -1e-9,
        "Alpha": 0.0,
        "Delta": 0.0,
        "asini": 10.0,
        "period": 864000.0,
        "tp": writer_kwargs["tstart"] + 0.5 * writer_kwargs["duration"],
        "h0": 1e-22,
        "cosi": 1,
        "psi": 0.0,
        "phi": 0.0,
        "tref": writer_kwargs["tstart"],
    }

@pytest.fixture
def writer(writer_kwargs, signal_parameters):
    writer = pyfstat.BinaryModulatedWriter(**writer_kwargs, **signal_parameters)
    writer.make_data()
    yield writer
    rmtree(writer.outdir)

def test_read_sfts(writer):
    power, timestamps, velocities, weights, t_sft, bin_0 = SFTDataIO(
        sftfilepath=writer.sftfilepath,
        freq_min=99.95,
        freq_max=100.05,
    )(sky_position=(0, 0))

    assert velocities.shape[0] == 3
    assert power.shape[1] == timestamps.shape[0]
    assert timestamps.shape[0] == weights.shape[0]