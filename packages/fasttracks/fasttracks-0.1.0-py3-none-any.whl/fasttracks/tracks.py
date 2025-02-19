import logging

import jax.numpy as jnp

logger = logging.getLogger(__name__)


def equatorial_to_cartesian(right_ascension, sin_declination):
    # -pi/2 < delta < pi/2 --> cos(delta) > 0
    cos_declination = jnp.sqrt(1 - sin_declination**2)
    return jnp.array(
        [
            [
                cos_declination * jnp.cos(right_ascension),
                cos_declination * jnp.sin(right_ascension),
                sin_declination,
            ]
        ]
    )


def f_of_t_isolated(theta, timestamps, velocities):
    """
    Parameters
    -------------
    theta:
        (f0, f1, ra, sin_dec, tref)
    timestamps:
        (num_timestamps,)
    velocities:
        (3, num_timestamps)
    """
    cartesian = equatorial_to_cartesian(theta[2], theta[3])
    return (theta[0] + (timestamps - theta[-1]) * theta[1]) * (
        1 + jnp.dot(cartesian, velocities).squeeze()
    )


def f_of_t_circular_binary(theta, timestamps, velocities):
    """
    Parameters
    -------------
    theta:
        (f0, ra, sin_dec, ap, omega, phib)

    phib is defined as `phib = omega * tasc`
    """
    cartesian = equatorial_to_cartesian(theta[1], theta[2])
    return theta[0] * (
        1
        + jnp.dot(cartesian, velocities).squeeze()
        - theta[3] * theta[4] * jnp.cos(theta[4] * timestamps - theta[5])
    )
