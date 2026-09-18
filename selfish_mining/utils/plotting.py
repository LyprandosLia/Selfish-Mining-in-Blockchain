import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_metrics(history : dict, save_prefix : str = 'thesis_fig'):

    plt.figure(figsize=(9, 4.5))
    rounds = history['round'][:100]
    beliefs = history['posterior_selfish'][:100]
    types = history['sender_type'][:100]

    colors = ['crimson' if t == 'theta_S' else 'navy' for t in types]
    plt.scatter(rounds, beliefs, c=colors, alpha=0.7, edgecolors='none', s=40)
    plt.axhline(y=0.5, color='gray', linestyle='--', label='Decision Threshold (0.5)')
    plt.title(r'Receiver Posterior Belief $\mu(\theta_S \mid \tau)$ over Rounds')
    plt.xlabel('Simulation Round')
    plt.ylabel(r'$P(\theta_S \mid \tau)$')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{save_prefix}_beliefs.png", dpi=300)
    plt.close()



def plot_equilibrium_boundary(R=10.0, c=2.0, kappa=0.5, save_path="thesis_fig_equilibrium.png"):
    # 2. Analytical Separating Equilibrium Contour Map (Section 4.3.2)
    alphas = np.linspace(1.0, 8.0, 500)
    gammas = np.linspace(0.0, 1.0, 500)
    A, G = np.meshgrid(alphas, gammas)
    
    tau_star = A / kappa
    
    threshold_gamma = ((kappa * tau_star) + c) / (R + A + c) 
    separating_region = G >= threshold_gamma

    plt.figure(figsize=(8, 5))
    plt.contourf(A, G, separating_region, cmap='coolwarm', alpha=0.7)
    plt.colorbar(label='1: Separating Equilibrium, 0: Non-Separating')
    
    plt.title(r'Separating PBE Region: $\gamma \geq \frac{\kappa \tau^* + c}{R + \alpha + c}$')
    plt.xlabel(r'Strategic Premium ($\alpha$)')
    plt.ylabel(r'Propagation Advantage ($\gamma$)')
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()