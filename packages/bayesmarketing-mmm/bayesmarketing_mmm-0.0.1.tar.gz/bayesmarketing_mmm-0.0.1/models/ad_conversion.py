import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def bayesian_conversion_model(clicks, impressions):
    """
    Bayesian Logistic Regression Model for Ad Conversion Rate Optimization.
    """
    alpha = numpyro.sample("alpha", dist.Normal(0, 1))
    beta = numpyro.sample("beta", dist.Normal(0, 1))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    theta = jnp.exp(alpha + beta * impressions) / (1 + jnp.exp(alpha + beta * impressions))
    numpyro.sample("obs", dist.Binomial(clicks, theta), obs=clicks)

def run_conversion_example():
    """
    Example usage of Bayesian Ad Conversion Model.
    """
    data = pd.DataFrame({
        "impressions": [100, 200, 300, 400, 500],
        "clicks": [5, 12, 25, 35, 50]
    })

    impressions = data["impressions"].values
    clicks = data["clicks"].values

    nuts_kernel = NUTS(bayesian_conversion_model)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), clicks, impressions)
    print(mcmc.get_samples())
