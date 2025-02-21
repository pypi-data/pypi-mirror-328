import numpy as np

class BayesianMultiArmedBandit:
    """
    Bayesian Multi-Armed Bandit using Thompson Sampling for optimal ad spend allocation.
    """
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.successes = np.zeros(num_arms)
        self.failures = np.zeros(num_arms)

    def select_arm(self):
        samples = [np.random.beta(self.successes[i] + 1, self.failures[i] + 1) for i in range(self.num_arms)]
        return np.argmax(samples)

    def update(self, arm, reward):
        if reward:
            self.successes[arm] += 1
        else:
            self.failures[arm] += 1

    def run_simulation(self, true_probs, num_rounds):
        rewards = []
        for _ in range(num_rounds):
            chosen_arm = self.select_arm()
            reward = np.random.rand() < true_probs[chosen_arm]
            self.update(chosen_arm, reward)
            rewards.append(reward)
        return rewards

# Example usage
if __name__ == "__main__":
    bandit = BayesianMultiArmedBandit(num_arms=3)
    true_probs = [0.2, 0.5, 0.8]  # True conversion rates of ads
    rewards = bandit.run_simulation(true_probs, num_rounds=1000)
    print(f"Total Reward: {sum(rewards)}")
