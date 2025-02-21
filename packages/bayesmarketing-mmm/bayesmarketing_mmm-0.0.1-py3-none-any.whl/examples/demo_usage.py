# Example Usage of BayesMarketing Library
# This script demonstrates how to use different models in the package.

from bayesmarketing.models import (
    advanced_mmm,
    multi_armed_bandit,
    clv_prediction,
    demand_forecasting,
    ad_conversion,
    geo_level_mmm,
    model_validation,
    seasonality,
    pareto_k_diagnostics,
    ucm_model,
)

# Run Advanced Bayesian MMM
print("Running Bayesian MMM Example...")
advanced_mmm.run_advanced_mmm()

# Run Bayesian Multi-Armed Bandit Simulation for Ad Budget Optimization
print("Running Bayesian Multi-Armed Bandit Example...")
bandit = multi_armed_bandit.BayesianMultiArmedBandit(num_arms=3)
true_probs = [0.2, 0.5, 0.8]  # True conversion rates of ads
rewards = bandit.run_simulation(true_probs, num_rounds=1000)
print(f"Total Reward: {sum(rewards)}")

# Run Bayesian Customer Lifetime Value (CLV) Prediction
print("Running Bayesian CLV Prediction Example...")
clv_prediction.run_clv_example()

# Run Bayesian Demand Forecasting
print("Running Bayesian Demand Forecasting Example...")
demand_forecasting.run_forecasting_example()

# Run Bayesian Ad Conversion Rate Optimization
print("Running Bayesian Ad Conversion Optimization Example...")
ad_conversion.run_conversion_example()

# Run Bayesian Geo-Level MMM
print("Running Bayesian Geo-Level MMM Example...")
geo_level_mmm.run_geo_mmm_example()

# Run Bayesian Model Validation with Posterior Predictive Checks
print("Running Bayesian Model Validation Example...")
model_validation.run_posterior_check_example()

# Run Bayesian Fourier-based Seasonality Model
print("Running Bayesian Seasonality Model Example...")
seasonality.run_seasonality_example()

# Run Pareto k Diagnostics & LOO-CV Example
print("Running Pareto k Diagnostics Example...")
pareto_k_diagnostics.run_pareto_k_example()

# Run Bayesian Unobserved Components Model (UCM) for Trend Analysis
print("Running Bayesian UCM Example...")
ucm_model.run_ucm_example()
