import logging
import time

import jax
import jax.numpy as jnp
import numpy as np
import matplotlib.pyplot as plt

import pyfstat
from fasttracks.dataio import SFTDataIO
from fasttracks import likelihood, tracks

logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s.%(msecs)03d %(name)s %(levelname)-8s: %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
)

# Create injection
writer_kwargs = {
    "label": "binaryAllSkyInjection",
    "outdir": "binaryAllSkyInjection",
    "tstart": 1368931380,
    "duration": 86400 * 30 * 1,
    "detectors": "H1,L1",
    "sqrtSX": 1e-23,
    "Tsft": 1800,
    "SFTWindowType": "tukey",
    "SFTWindowParam": 0.01,
    "Band": 2.0,
}

signal_kwargs = {
    "F0": 100.0,
    "F1": 0,
    "asini": 10.0,
    "period": 864000.0,
    "tp": writer_kwargs["tstart"] + 0.5 * writer_kwargs["duration"],
    "h0": writer_kwargs["sqrtSX"] / 5.0,
    "psi": 0,
    "cosi": 1,
    "phi": 0,
    "Alpha": 0.0,
    "Delta": 0.0,
}
writer = pyfstat.BinaryModulatedWriter(**writer_kwargs, **signal_kwargs)
writer.make_data()

targeted_theta = jnp.array(
    [signal_kwargs[key] for key in ["F0", "Alpha", "Delta", "asini", "period", "tp"]]
)
targeted_theta = targeted_theta.at[2].set(jnp.sin(targeted_theta[2]))
targeted_theta = targeted_theta.at[4].set(2 * jnp.pi / targeted_theta[4])
targeted_theta = targeted_theta.at[5].set(
    targeted_theta[4] * targeted_theta[5]
)  # phib = Omega * tasc

dvalues = jnp.zeros(len(targeted_theta))
dvalues = dvalues.at[3].set(2)
dvalues = dvalues.at[4].set(1e-6)
dvalues = dvalues.at[5].set(jnp.pi)

upper_vals = targeted_theta + dvalues
lower_vals = targeted_theta - dvalues


def get_batch(key):
    key, subkey = jax.random.split(key)
    return key, jax.random.uniform(
        subkey,
        shape=(batch_size, 6),
        minval=lower_vals,
        maxval=upper_vals,
    )


# Compute detection statistics
power, timestamps, velocities, weights, t_sft, bin_0 = SFTDataIO(
    sftfilepath=writer.sftfilepath,
    freq_min=99.95,
    freq_max=100.05,
)(sky_position=(signal_kwargs["Alpha"], signal_kwargs["Delta"]))


def statistic(template):
    track_hertz = tracks.f_of_t_circular_binary(template, timestamps, velocities)
    return likelihood.normalized_power(track_hertz, weights, power, t_sft, bin_0)


fast_statistic = jax.jit(jax.vmap(statistic, in_axes=0, out_axes=0))

key = jax.random.PRNGKey(0)
batch_size = 50000
num_batches = 10
num_templates = batch_size * num_batches

templates = jnp.zeros((num_templates, 6))
powers = jnp.zeros(num_templates)

logging.info(f"Num. templates: {num_templates}")
logging.info("Starting compute statistic for loop")

for ind in range(num_batches):
    key, batch_thetas = get_batch(key)

    t0 = time.time()
    batch_power = fast_statistic(batch_thetas).block_until_ready()
    logging.info(f"Time to run a batch: {time.time() - t0:.2g} s")

    left = ind * batch_size
    right = left + batch_size

    templates = templates.at[left:right].set(batch_thetas)
    powers = powers.at[left:right].set(batch_power)

logging.info("Done!")

logging.info(f"Computing targeted track power")
targeted_track = tracks.f_of_t_circular_binary(targeted_theta, timestamps, velocities)
targeted_power = likelihood.normalized_power(
    targeted_track, weights, power, t_sft, bin_0
)

# Make a plot of the targeted_power results
logging.info(f"Generating templates vs power plot")
sort_ind = jnp.argsort(powers)
stat = powers[sort_ind]
aps = templates[:, 3][sort_ind]
pds = 2 * jnp.pi / templates[:, 4][sort_ind]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
scattering = axs[1, 0].scatter(pds, aps, c=stat, cmap="coolwarm")
axs[0, 0].scatter(pds, stat, c=stat, cmap="coolwarm")
axs[0, 0].scatter(signal_kwargs["period"], targeted_power, c="r", marker="*")
axs[1, 1].scatter(stat, aps, c=stat, cmap="coolwarm")
axs[1, 1].scatter(targeted_power, signal_kwargs["asini"], c="r", marker="*")

axs[1, 0].set(
    xlabel="Orbital Period (s)",
    ylabel="Projected Semimajor Axis (s)",
)
axs[1, 1].set(
    ylabel="Projected Semimajor Axis (s)",
    xlabel="Weighed Normalized Power",
)
axs[0, 0].set(
    xlabel="Orbital Period (s)",
    ylabel="Weighed Normalized Power",
)
axs[0, 0].axvline(signal_kwargs["period"], ls="--", c="k", lw=1, alpha=0.9)
axs[1, 0].axhline(signal_kwargs["asini"], ls="--", c="k", lw=1, alpha=0.9)
axs[1, 0].axvline(signal_kwargs["period"], ls="--", c="k", lw=1, alpha=0.9)
axs[1, 1].axhline(signal_kwargs["asini"], ls="--", c="k", lw=1, alpha=0.9)
axs[0, 1].axis("off")
for ax in axs.flat:
    ax.grid(which="major", ls="-", alpha=0.2)
    ax.grid(which="minor", ls="-", alpha=0.1)
    ax.minorticks_on()
fig.colorbar(scattering, label="power", ax=axs[0, 1], location="left")
fig.savefig(f"{writer_kwargs['outdir']}/batch_power.png")

# Make a plot of the generated data
# This concatenates all detectors, it is what it is.
logging.info(f"Generating spectrogram plot")
fig, ax = plt.subplots(figsize=(16, 10))
c = ax.pcolormesh(power)
targeted_track_bins = (targeted_track * t_sft + 0.5).astype("uint32") - bin_0
ax.plot(
    targeted_track_bins + 1,
    color="white",
    label="Injected Signal",
    lw=0.5,
)
ax.plot(
    targeted_track_bins - 1,
    color="white",
    lw=0.5,
)
fig.colorbar(c)
fig.tight_layout()
fig.savefig(f"{writer_kwargs['outdir']}/spectrogram.png")

logging.info(f"All done")
