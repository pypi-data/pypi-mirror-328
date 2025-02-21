import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def adstock(x, decay):
    return jnp.convolve(x, jnp.exp(-decay * jnp.arange(len(x))), mode="same")

def hill_function(spend, alpha, beta):
    return alpha * (spend ** beta) / (spend ** beta + 1)

def bayesian_mmm(tv, digital, social, sales):
    intercept = numpyro.sample("intercept", dist.Normal(0, 1))
    decay = numpyro.sample("decay", dist.Beta(2, 2))
    alpha_tv = numpyro.sample("alpha_tv", dist.HalfNormal(1.0))
    beta_tv = numpyro.sample("beta_tv", dist.Beta(2, 2))
    alpha_digital = numpyro.sample("alpha_digital", dist.HalfNormal(1.0))
    beta_digital = numpyro.sample("beta_digital", dist.Beta(2, 2))
    alpha_social = numpyro.sample("alpha_social", dist.HalfNormal(1.0))
    beta_social = numpyro.sample("beta_social", dist.Beta(2, 2))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    tv_effect = hill_function(adstock(tv, decay), alpha_tv, beta_tv)
    digital_effect = hill_function(adstock(digital, decay), alpha_digital, beta_digital)
    social_effect = hill_function(adstock(social, decay), alpha_social, beta_social)

    mu = intercept + tv_effect + digital_effect + social_effect
    numpyro.sample("obs", dist.Normal(mu, sigma), obs=sales)

def run_advanced_mmm():
    data = pd.read_csv("bayesmarketing/datasets/mmm_sample.csv")
    tv = data["tv_ad_spend"].values
    digital = data["digital_ad_spend"].values
    social = data["social_ad_spend"].values
    sales = data["sales"].values

    nuts_kernel = NUTS(bayesian_mmm)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), tv, digital, social, sales)
    print(mcmc.get_samples())
