"""
Entropic Gravity Simulation - 1D Emergent Gravity
-------------------------------------------------
Based on Erik Verlinde's Entropic Gravity Theory

This module implements a basic 1D simulation where gravity emerges
from entropy maximization, without programming forces directly.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- ENTROPIC UNIVERSE CONFIGURATION ---
# No constant G. No Newton's Law here.
# Only Probability.

MASS_POSITION = 0.0      # The center of the universe (Where information is dense)
INITIAL_POSITION = 50.0  # Where we release the particle
STEPS = 2000             # Number of simulation steps

def information_density(x):
    """
    According to Verlinde, entropy changes with distance.
    Near the mass, the density of holographic bits is higher.
    This creates an 'entropy gradient'.

    Parameters:
    -----------
    x : float
        Particle position

    Returns:
    --------
    float
        Information density (proportional to entropy)
    """
    # Avoid division by zero
    distance = abs(x - MASS_POSITION)
    if distance < 1.0:
        return 10000.0  # Increased for stronger gradient

    # Improved model: Entropy (S) is proportional to 1/r^2
    # Simulating gravitational force ~1/r^2
    return 1.0 / (distance ** 2)

def simulate_entropic_fall(initial_position=None, steps=None, temperature=0.1, verbose=False):
    """
    Simulates the entropic fall of a particle towards the center of mass.

    Parameters:
    -----------
    initial_position : float, optional
        Initial particle position (default: INITIAL_POSITION)
    steps : int, optional
        Number of simulation steps (default: STEPS)
    temperature : float, optional
        System temperature (thermal agitation)
    verbose : bool, optional
        Print progress

    Returns:
    --------
    list
        Particle trajectory over time
    """
    if initial_position is None:
        initial_position = INITIAL_POSITION
    if steps is None:
        steps = STEPS

    position = initial_position
    trajectory = [position]

    for i in range(steps):
        # 1. Propose a random movement (Pure Random Walk)
        step = np.random.choice([-1, 1]) * 0.5
        new_position_proposed = position + step

        # 2. Calculate Entropy Change (Delta S)
        # S_current vs S_new
        S_current = information_density(position)
        S_new = information_density(new_position_proposed)

        delta_S = S_new - S_current

        # 3. The Thermodynamic Rule (Entropic Force)
        # The system prefers to go where Entropy is higher (near the mass).
        # We use Metropolis to accept the movement

        # If entropy increases (delta_S > 0), always accept.
        # If it decreases, accept with a small probability.
        if delta_S > 0 or np.random.rand() < np.exp(delta_S / temperature):
            position = new_position_proposed

        trajectory.append(position)

        # If touched the mass, stop
        if abs(position - MASS_POSITION) < 1.0:
            if verbose:
                print(f"Impact at step {i}")
            break

    return trajectory

def plot_simulation(trajectory, save_figure=False, filename='results/entropic_gravity_simulation.png'):
    """
    Plots the simulation trajectory.

    Parameters:
    -----------
    trajectory : list
        Particle trajectory
    save_figure : bool, optional
        If True, saves variable to file
    filename : str, optional
        Filename to save figure
    """
    plt.figure(figsize=(10, 6))
    plt.plot(trajectory, label='Particle Trajectory')
    plt.axhline(y=MASS_POSITION, color='r', linestyle='--', label='Center of Mass (High Entropy)')
    plt.title('Entropic Gravity Simulation (Verlinde)\nNo G Force, only Entropy Maximization')
    plt.xlabel('Time (Steps)')
    plt.ylabel('Distance')
    plt.legend()
    plt.grid(True, alpha=0.3)

    if save_figure:
        import os
        os.makedirs('results', exist_ok=True)
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Figure saved as {filename}")

    plt.show()

if __name__ == "__main__":
    # --- EXECUTION AND PROOF ---
    print("Running emergent gravity simulation...")
    history = simulate_entropic_fall(verbose=True)

    print(f"Simulation completed. Final trajectory: {len(history)} steps")
    print(f"Final Position: {history[-1]:.2f}")

    plot_simulation(history, save_figure=True)
