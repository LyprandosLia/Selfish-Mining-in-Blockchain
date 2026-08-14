import numpy as np
from game.signalling import ThesisSignalEngine

class SenderPool:
    def __init__(self, q: float, alpha: float, kappa: float, epsilon: float):
        self.q = q
        self.alpha = alpha
        self.kappa = kappa
        self.epsilon = epsilon

    def sample_type(self) -> str:
        """Nature selects player type theta_H with prob q or theta_S with prob 1-q."""
        return 'theta_H' if np.random.rand() < self.q else 'theta_S'

    def emit_signal(self, sender_type :str):
        """
        Generates signal delay tau.
        Honest Pool (theta_H): tau = 0 (unintentional noise produces tau > 0 with prob epsilon).[cite: 1]
        Selfish Pool (theta_S): tau = tau* = alpha / kappa.[cite: 1]
        """
        tau_star = ThesisSignalEngine.optimal_withholding_threshold(self.alpha, self.kappa)

        if sender_type == 'theta_H':
            if np.random.rand() < self.epsilon:
                return np.random.uniform(0.01, tau_star)
            return 0.0
        else:
            return tau_star

class NetworkReceiver:
    def __init__(self, R_net : float, belief_threshold : float = 0.5):
        self.R_net = R_net
        self.threshold = belief_threshold

    def evaluate_and_decide(self, tau: float, epsilon: float, q: float)->tuple[str, float]:
        """
        Updates posterior belief P(theta_S | tau) via Bayes' Rule and selects
        action 'Follow' or 'Ignore' (Section 4.2.5).[cite: 1]
        """
        if tau == 0.0:
            posterior_selfish = 0.0
        else:
            prior_selfish = 1.0 - q
            prior_honest = q
            denom = (prior_selfish * 1.0) + (prior_honest * epsilon)
            posterior_selfish = (prior_selfish * 1.0) / denom if denom > 0 else prior_selfish

        action = 'Ignore' if posterior_selfish >= self.threshold else 'Follow'
        return action, posterior_selfish
        