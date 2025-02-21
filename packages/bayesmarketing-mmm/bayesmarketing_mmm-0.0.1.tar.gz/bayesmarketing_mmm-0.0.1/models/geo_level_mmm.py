import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def hierarchical_bayesian_mmm(region, tv, digital, social, sales):
    """
    Hierarchical Bayesian MMM for Geo-Level Modeling.
    """
    region_mu = numpyro.sample("region_mu", dist.Normal(0, 1), sample_shape=(len(set(region)),))
    region_sigma = numpyro.sample("region_sigma", dist.HalfNormal(1.0))

    intercept = numpyro.sample("intercept", dist.Normal(region_mu[region], region_sigma))
    beta_tv = numpyro.sample("beta_tv", dist.Normal(0, 1))
    beta_digital = numpyro.sample("beta_digital", dist.Normal(0, 1))
    beta_social = numpyro.sample("beta_social", dist.Normal(0, 1))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    mu = intercept + beta_tv * tv + beta_digital * digital + beta_social * social

    numpyro.sample("obs", dist.Normal(mu, sigma), obs=sales)

def run_geo_mmm_example():
    """
    Example usage of Geo-Level Bayesian MMM.
    """
    data = pd.DataFrame({
        "region": [0, 1, 0, 1, 2],
        "tv_ad_spend": [100, 200, 150, 300, 250],
        "digital_ad_spend": [50, 120, 100, 250, 200],
        "social_ad_spend": [20, 80, 70, 150, 130],
        "sales": [500, 800, 750, 1200, 1100]
    })

    region = data["region"].values
    tv = data["tv_ad_spend"].values
    digital = data["digital_ad_spend"].values
    social = data["social_ad_spend"].values
    sales = data["sales"].values

    nuts_kernel = NUTS(hierarchical_bayesian_mmm)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), region, tv, digital, social, sales)
    print(mcmc.get_samples())
