import jax.numpy as jnp

def normalized_power(track_hertz, weights, power, t_sft, bin_0):
    track_bins = (track_hertz * t_sft + 0.5).astype("uint32") - bin_0
    return jnp.sum(weights * power[track_bins,  jnp.arange(track_hertz.shape[0])])
