import numpyro
import numpyro.distributions as dist
import jax.numpy as jnp
from numpyro.infer import MCMC, NUTS
import pandas as pd
from jax import random

def fourier_series(time, order=3):
    """
    Generate Fourier series terms for seasonality modeling.
    """
    terms = []
    for i in range(1, order + 1):
        terms.append(jnp.sin(2 * jnp.pi * i * time))
        terms.append(jnp.cos(2 * jnp.pi * i * time))
    return jnp.stack(terms, axis=-1)

def bayesian_seasonality_model(time, sales):
    """
    Bayesian Time-Series Model with Fourier-based Seasonality.
    """
    fourier_terms = fourier_series(time, order=3)
    beta = numpyro.sample("beta", dist.Normal(0, 1), sample_shape=(fourier_terms.shape[1],))
    intercept = numpyro.sample("intercept", dist.Normal(0, 1))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    mu = intercept + jnp.dot(fourier_terms, beta)
    numpyro.sample("obs", dist.Normal(mu, sigma), obs=sales)

def run_seasonality_example():
    """
    Example usage of Bayesian Seasonality Model.
    """
    data = pd.DataFrame({
        "time": jnp.arange(1, 13),
        "sales": jnp.array([100, 120, 150, 180, 210, 250, 280, 300, 260, 220, 180, 140])
    })

    time = data["time"].values
    sales = data["sales"].values

    nuts_kernel = NUTS(bayesian_seasonality_model)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), time, sales)
    print(mcmc.get_samples())
