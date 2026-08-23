# =============================================================================
# Protocol Economic Incentives
# =============================================================================
R: float = 10.0            # Block Reward distributed for a valid block
ALPHA: float = 3.0         # Strategic Premium gained from private chain extension
C: float = 8.5             # Cost of Mining (electricity & hardware, deliberately
                            # set close to R to stress-test the model near its
                            # domain boundary c < R, Section 4.2.5)

# =============================================================================
# Delay & Signaling Costs
# =============================================================================
KAPPA: float = 0.5         # Marginal Delay Cost (risk coefficient per unit time)
                            # Note: Total Signaling Cost (KAPPA * tau) is computed
                            # dynamically via optimal_withholding_threshold().

# =============================================================================
# Network & Game Properties
# =============================================================================
GAMMA: float = 0.4         # Propagation Advantage in [0, 1] (Eyal & Sirer, 2013).
                            # NOTE: at baseline ALPHA/KAPPA/C values, the derived
                            # threshold gamma* (Section 4.3.2) is ~0.674 -- this
                            # value sits BELOW that threshold, so the model
                            # predicts pooling, not separation, at this setting.
R_NET: float = 10.0        # Network Payoff when honest decisions succeed

# =============================================================================
# Belief Structure (Section 4.2.1)
# =============================================================================
Q: float = 0.7             # Prior belief P(theta_H) that the Sender is Honest.
                            # This is NOT hashrate share -- see HASHRATE_SHARE
                            # below for the population-level mining-power variable.
EPSILON: float = 0.1       # Network noise probability, P(tau > 0 | theta_H)

# =============================================================================
# Population Structure (Chapter 5 simulation only -- not part of the
# theoretical signaling game itself)
# =============================================================================
HASHRATE_SHARE: float = 0.3   # Fraction of total hashrate controlled by the
                               # Selfish population, used only to determine
                               # which pool discovers each block in the
                               # simulation loop. Distinct from Q.

# =============================================================================
# Simulation Control Parameters
# =============================================================================
ROUNDS: int = 5000
RANDOM_SEED: int = 7
RECEIVER_THRESHOLD: float = 0.5   # Posterior-belief cutoff for the Receiver's
                                   # Follow/Ignore decision (see Section 5.3.4
                                   # for the simplification this represents
                                   # relative to a full expected-utility rule).