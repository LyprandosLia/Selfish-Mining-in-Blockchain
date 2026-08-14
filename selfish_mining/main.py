import numpy as np
import config
from simulation.engine import ThesisSimulationEngine
from utils.plotting import plot_simulation_metrics, plot_equilibrium_boundary

def main():
    print("==========================================================")
    print("  Game-Theoretic Selfish Mining Simulation Engine")
    print("  Based on Thesis Signaling Model (Sections 4 & 5)")
    print("==========================================================")
    
    np.random.seed(config.RANDOM_SEED)
    
    # Run the simulation engine
    engine = ThesisSimulationEngine()
    results = engine.run_simulation(num_rounds=config.ROUNDS)
    
    # Compute accuracy & metrics
    total_rounds = len(results['round'])
    correct_actions = sum(
        1 for stype, act in zip(results['sender_type'], results['action'])
        if (stype == 'theta_S' and act == 'Ignore') or (stype == 'theta_H' and act == 'Follow')
    )
    accuracy = (correct_actions / total_rounds) * 100
    rev = results['relative_revenue']
    
    print(f"Total Blocks Simulated      : {total_rounds}")
    print(f"Receiver Detection Accuracy : {accuracy:.2f}%")
    print(f"Main Chain Canonical Blocks : {rev['total_main_blocks']}")
    print(f"Selfish Pool Revenue Share  : {rev['selfish_share']*100:.2f}%")
    print(f"Honest Network Revenue Share: {rev['honest_share']*100:.2f}%")
    print(f"Mean Sender Utility U_S     : {np.mean(results['u_sender']):.2f}")
    print(f"Mean Receiver Utility U_R   : {np.mean(results['u_receiver']):.2f}")
    print("----------------------------------------------------------")
    
    # Generate charts for thesis Chapter 5
    plot_simulation_metrics(results)
    plot_equilibrium_boundary(config.R, config.C, config.KAPPA)
    print("Generated figures: 'thesis_fig_beliefs.png' and 'thesis_fig_equilibrium.png'")

if __name__ == '__main__':
    main()