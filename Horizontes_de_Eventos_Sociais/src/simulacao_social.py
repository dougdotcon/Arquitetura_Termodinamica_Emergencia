"""
Social Ising Model Simulation (Opinion Dynamics)
------------------------------------------------
Author: Antigravity (AI Theoretical Physicist)
Date: 2025-12-27

Objective:
Simulate the formation of social consensus and polarization using the 2D Ising Model.

Theory:
- Societal Agents: Spins on a 2D grid (+1: Opinion A, -1: Opinion B).
- Social Pressure (J): Tendency to align with neighbors (Conformity).
- External Field (H): Mass Media or Propaganda.
- Social Temperature (T): Randomness/Noise/Anomia in society.

Algorithm:
- Metropolis-Hastings Monte Carlo.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from numba import njit

# --- Constants ---
GRID_SIZE = 50           # 50x50 agents = 2500 people
J = 1.0                  # Interaction strength (Social Coupling)
STEPS_PER_TEMP = 100000  # Monte Carlo steps per temperature
OUTPUT_DIR = r"C:\Users\Douglas\Desktop\Entropy\Horizontes_de_Eventos_Sociais\results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

@njit
def energy(grid, H):
    """Calculate total Hamiltonian of the social grid."""
    # Sum over nearest neighbors
    # H = -J * sum(s_i * s_j) - H * sum(s_i)
    interaction = 0.0
    N = grid.shape[0]
    for i in range(N):
        for j in range(N):
            S = grid[i, j]
            # Periodic Boundary Conditions (Toroidal Society - e.g., Internet Bubble)
            nb = grid[(i+1)%N, j] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[i, (j-1)%N]
            interaction += -J * S * nb
    
    # Each pair counted twice, so divide by 2
    return interaction / 2.0 - H * np.sum(grid)

@njit
def metropolis_step(grid, T, H):
    """
    Execute one Metropolis-Hastings step (sweep over N^2 sites).
    Returns change in magnetization if any.
    """
    N = grid.shape[0]
    beta = 1.0 / T if T > 0 else 1e9
    
    for _ in range(N * N): # One sweep
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
        s = grid[i, j]
        
        # Calculate delta E for flipping spin s -> -s
        # Only local neighbors matter for delta E
        nb = grid[(i+1)%N, j] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[i, (j-1)%N]
        dE = 2 * s * (J * nb + H)
        
        if dE < 0 or np.random.random() < np.exp(-dE * beta):
            grid[i, j] *= -1 # Flip

@njit
def run_hysteresis_loop(h_range, T):
    """
    Simulate Hysteresis: Vary field H from -H_max to +H_max and back.
    Demonstrates Social Inertia.
    """
    N = GRID_SIZE
    grid = np.random.choice(np.array([-1, 1], dtype=np.int8), size=(N, N))
    
    n_steps = len(h_range)
    magnetizations = np.zeros(2 * n_steps)
    
    # Forward path
    idx = 0
    for h in h_range:
        for _ in range(100): # Equilibrate faster
            metropolis_step(grid, T, h)
        m = np.sum(grid) / (N*N)
        magnetizations[idx] = m
        idx += 1
        
    # Backward path
    h_reversed = h_range[::-1]
    for h in h_reversed:
        for _ in range(100):
            metropolis_step(grid, T, h)
        m = np.sum(grid) / (N*N)
        magnetizations[idx] = m
        idx += 1
        
    return np.concatenate((h_range, h_reversed)), magnetizations, grid

def plot_hysteresis(h_values, m_values, T):
    plt.figure(figsize=(10, 6))
    
    # Split forward and backward for coloring
    split = len(h_values) // 2
    
    plt.plot(h_values[:split], m_values[:split], 'b.-', label='Rising Propaganda (H -> +)')
    plt.plot(h_values[split:], m_values[split:], 'r.-', label='Falling Propaganda (H -> -)')
    
    plt.axvline(0, color='k', linestyle='--', alpha=0.3)
    plt.axhline(0, color='k', linestyle='--', alpha=0.3)
    plt.xlabel('External Field $H$ (Propaganda/Bias)')
    plt.ylabel('Magnetization $M$ (Public Consensus)')
    plt.title(f'Social Hysteresis Loop at T={T:.1f}\n(Inertia of Public Opinion)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_path = os.path.join(OUTPUT_DIR, f'social_hysteresis_T{T}.png')
    plt.savefig(output_path)
    print(f"[RESULT] Hysteresis plot saved to: {output_path}")

def plot_society_snapshot(grid, T):
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap='coolwarm', interpolation='nearest')
    plt.title(f'Social Fabric Snapshot (T={T})')
    plt.axis('off')
    
    output_path = os.path.join(OUTPUT_DIR, f'social_snapshot_T{T}.png')
    plt.savefig(output_path)
    print(f"[RESULT] Snapshot saved to: {output_path}")

if __name__ == "__main__":
    print("=== Social Ising Model Simulation ===")
    
    # 1. Phase Transition Check (Critical T approx 2.269 for Ising)
    # We choose T < Tc to show Hysteresis
    T_sim = 1.8 
    
    print(f"[INFO] Running Hysteresis Loop at T={T_sim} (Below Critical Temp)...")
    
    h_max = 2.0
    h_steps = 50
    h_range = np.linspace(-h_max, h_max, h_steps)
    
    h_vals, m_vals, final_grid = run_hysteresis_loop(h_range, T_sim)
    
    plot_hysteresis(h_vals, m_vals, T_sim)
    plot_society_snapshot(final_grid, T_sim)
