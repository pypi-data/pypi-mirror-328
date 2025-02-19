import jax
import jax.numpy as jnp
import pytest

from fasttracks import tracks


@pytest.fixture
def timestamps():
    return jnp.arange(1000)


@pytest.fixture
def velocities(timestamps):
    return jnp.ones((3, timestamps.shape[0]))


@pytest.fixture
def theta_isolated():
    return jnp.array([100.0, 0.0, 0.0, 0.0, 0.0])


@pytest.fixture
def batch_isolated():
    return jnp.vstack([jnp.array([100.0, 0.0, 0.0, 0.0, 0.0]) for i in range(10)])


def test_isolated_track(theta_isolated, timestamps, velocities):
    tracks.f_of_t_isolated(theta_isolated, timestamps, velocities)

def test_vmap_track(batch_isolated, timestamps, velocities):
    batch_out = jax.vmap(tracks.f_of_t_isolated, in_axes=(0, None, None), out_axes=0)(
        batch_isolated, timestamps, velocities
    )
    print(batch_out)
    print(batch_out.shape)
    assert batch_out.shape[0] == batch_isolated.shape[0]
