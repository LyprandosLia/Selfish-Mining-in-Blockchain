
# Protocol Economic Incentives
R: float = 10.0           # Block Reward distributed for a valid block
ALPHA: float = 3.0        # Strategic Premium gained from private chain extension
# C: float = 2.0            # Cost of Mining (electricity & hardware operational cost)
C: float = 8.5            # High cost of mining (electricity/hardware is very expensive)


# Delay & Signaling Costs
KAPPA: float = 0.5        # Marginal Delay Cost (risk coefficient per unit time)
                          # Note: Total Signaling Cost (KAPPA * tau) is computed dynamically.[cite: 1]

# Network & Game Properties
GAMMA: float = 0.4        # Propagation Advantage in [0, 1] (Eyal & Sirer, 2013)[cite: 1]
R_NET: float = 10.0       # Network Payoff when honest decisions succeed[cite: 1]

# Signaling Noise & Information Structure
# EPSILON: float = 0.1      # Network noise probability P(tau > 0 | theta_H)[cite: 1]
# Q: float = 0.8            # Prior belief probability P(theta_H)[cite: 1]
# EPSILON: float = 0.8      # High network lag (perfect camouflage for the attacker)
# Q: float = 0.7            # Selfish miner now has 30% of the hashpower
# --- Dataset 4: The Unprofitable Attack ---
Q: float = 0.7            # Attacker has 30% hashpower
EPSILON: float = 0.1      # Low noise, network can detect the attack easily

#Simulation Control Parameters
ROUNDS : int = 5000
RANDOM_SEED : int = 42
RECEIVER_THRESHOLD: float = 0.5
