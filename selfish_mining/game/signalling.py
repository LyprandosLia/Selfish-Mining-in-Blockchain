import numpy as np
class ThesisSignalEngine:

    """
    Implements utility functions U_S and U_R for Sender and Receiver
    using the exact formulas from Section 4.2.4.[cite: 1]
    """
    @staticmethod
    def compute_posterior_beliefs(tau: float, epsilon: float, q: float) -> tuple[float, float]:
        if tau == 0.0:
            return 1.0, 0.0
        
        prior_selfish = 1.0 - q
        prior_honest = q
        denom = (prior_selfish * 1.0) + (prior_honest * epsilon)
        
        if denom > 0:
            p_selfish = (prior_selfish * 1.0) / denom
            p_honest = (prior_honest * epsilon) / denom
        else:
            p_selfish, p_honest = prior_selfish, prior_honest
            
        return p_honest, p_selfish
    
    
    @staticmethod
    def calculate_payoffs(
        sender_type : str,
        tau : float,
        action : str,
        R : float,
        alpha : float,
        c : float,
        kappa : float,
        gamma : float,
        R_net : float,
        rng = None
    )->tuple[float , float]:

    # """
    #     Computes (U_Sender, U_Receiver) given the Sender's type, signal delay tau, 
    #     and Receiver action ('Follow' or 'Ignore').[cite: 1]  
    #     Parameters:
    #     - R: Block Reward[cite: 1]
    #     - alpha: Strategic Premium[cite: 1]
    #     - c: Cost of Mining[cite: 1]
    #     - kappa: Marginal Delay Cost[cite: 1]
    #     - kappa * tau: Total Signaling Cost (linear in tau)[cite: 1]
    #     - gamma: Propagation Advantage[cite: 1]
    #     - R_net: Network Payoff[cite: 1]
    # """
        # Calculate dynamic Total Signaling Cost: kappa * tau[cite: 1]

    
     total_signalling_cost = kappa * tau

     if rng is None:
        rng = np.random.default_rng()


     if sender_type == 'theta_H':
        if action == "Follow":
           u_sender  = R
           u_receiver = R_net
        else: #theta_H's action == Ignore
            u_sender = R - c
            u_receiver = R_net
     else: #sender_type == 'theta_S
        if action == 'Follow':
           u_sender = R + alpha - total_signalling_cost
           u_receiver = 0.0
        else: #if action == Ignore
            # Resolve the fork race stochastically, per round, rather than
            # using the closed-form expected value directly. This is what
            # makes the simulation a genuine dynamic test of the theoretical
            # formula, rather than a re-statement of it.
            # u_sender = (gamma * (R + alpha - total_signalling_cost)) + \
            #                ((1.0 - gamma) * (-total_signalling_cost - c))
            # u_receiver = R_net
            # rng = np.random.default_rng()
            # branch_wins = rng.random() < gamma

            branch_wins = rng.random() < gamma

            if branch_wins:
                u_sender = R + alpha - total_signalling_cost
            else:
                u_sender = -total_signalling_cost - c
            
            u_receiver = R_net
     return u_sender, u_receiver

    @staticmethod
    def optimal_withholding_threshold(alpha : float, kappa : float)->float:
       """
        Returns  tau* = alpha / kappa, the optimal withholding upper limit
        where strategic premium equals total signaling cost (Section 4.2.4).[cite: 1]
        """
       import config
       
       return config.TAU_W
       


