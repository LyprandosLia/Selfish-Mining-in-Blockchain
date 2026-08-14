import numpy as np
import config
from agents.miner import SenderPool, NetworkReceiver
from game.signalling import ThesisSignalEngine
from models.chain import Blockchain

class ThesisSimulationEngine:
    def __init__(self):
        self.chain = Blockchain()
        self.sender = SenderPool(config.Q, config.ALPHA, config.KAPPA, config.EPSILON)
        self.receiver = NetworkReceiver(config.R_NET, config.RECEIVER_THRESHOLD)

    def run_simulation(self, num_rounds : int = config.ROUNDS)->dict:
        history = {
            'round' : [],
            'sender_type' : [],
            'tau' : [],
            'posterior_selfish' : [],
            'action' : [] ,
            'u_sender' : [],
            'u_receiver' : [],
            'private_lead' : [],
            'relative_revenue' : []
        }

        for i in range(1, num_rounds + 1):
            sender_type = self.sender.sample_type()
            tau = self.sender.emit_signal(sender_type)
            is_private = (sender_type == 'theta_S')

            #Step 1 : Add the block to the chain
            self.chain.add_block(miner_type=sender_type, delay_tau = tau, is_private= is_private)

            #Step 2 : Receiver evaluates signal delay and chooses action
            action, p_selfish = self.receiver.evaluate_and_decide(tau, config.EPSILON, config.Q)

            #Step 3 : Resolve chain fork
            self.chain.resolve_fork(receiver_action=action)

            #Step 4 : Calculate payoffs
            u_s , u_r = ThesisSignalEngine.calculate_payoffs(
                sender_type , tau, action,
                config.R, config.ALPHA, config.C, config.KAPPA,
                config.GAMMA, config.R_NET
            )

            history['round'].append(i)
            history['sender_type'].append(sender_type)
            history['action'].append(action)
            history['tau'].append(tau)
            history['posterior_selfish'].append(p_selfish)
            history['u_sender'].append(u_s)
            history['u_receiver'].append(u_r)
            history['private_lead'].append(self.chain.private_lead)

        history['relative_revenue'] = self.chain.calculate_relative_revenue()
        return history