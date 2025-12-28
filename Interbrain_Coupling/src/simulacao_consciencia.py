"""
Thermodynamics of Consciousness Simulation (Kuramoto Model)
-----------------------------------------------------------
Author: Antigravity (AI Theoretical Physicist)
Date: 2025-12-27

Objective:
Simulate synchronization phase transition (Emergence of Consciousness)
using the Kuramoto Model with Langevin Noise.

Theory:
- Oscilators: Agents/Neurons with intrinsic frequency omega.
- Coupling (K): Empathy / Synaptic Strength.
- Noise (D): Thermal Entropy / Stress.
- Order Parameter (r): Measure of coherence (0=Chaos, 1=Global Consciousness).

Dynamics:
d(theta_i)/dt = omega_i + (K/N)*sum(sin(theta_j - theta_i)) + noise
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from numba import njit

# --- Constants ---
N = 200                 # Number of oscillators
DT = 0.05               # Time step
STEPS = 5000            # Integration steps per simulation
OUTPUT_DIR = r"C:\Users\Douglas\Desktop\Entropy\Acoplamento_Intercerebral\results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

@njit
def kuramoto_step(theta, omega, K, D, dt):
    """
    Update phases using Euler-Maruyama integration.
    theta: array of phases
    omega: intrinsic frequencies
    K: coupling strength
    D: noise intensity (variance of Weiner process)
    """
    N = len(theta)
    d_theta = np.zeros(N)
    
    # Calculate interaction term sum(sin(theta_j - theta_i))
    # This is O(N^2). For N=200, N^2=40000, perfectly fine.
    for i in range(N):
        interaction = 0.0
        for j in range(N):
            interaction += np.sin(theta[j] - theta[i])
        
        # Stochastic term: sqrt(2D dt) * Gaussian
        noise = np.sqrt(2 * D * dt) * np.random.randn()
        
        d_theta[i] = omega[i] + (K / N) * interaction + noise
        
    return theta + d_theta * dt

@njit
def calc_order_parameter(theta):
    """
    Calculate complex order parameter z = r * e^(i*psi)
    Returns magnitude r.
    """
    N = len(theta)
    # sum e^(i theta)
    # e^(ix) = cos(x) + i sin(x)
    z_real = np.sum(np.cos(theta)) / N
    z_imag = np.sum(np.sin(theta)) / N
    return np.sqrt(z_real**2 + z_imag**2)

def run_phase_transition_experiment():
    """
    Vary Coupling K and measure average Order Parameter <r>.
    Demonstrates the transition from Incoherent (r~0) to Synchronized (r~1).
    """
    print("[INFO] Starting Phase Transition Experiment...")
    
    # Parameters
    omega = np.random.normal(0, 1.0, N) # Natural frequencies, Normal(0, 1)
    # Theoretically, Kc = 2 / (pi * g(0)) for Lorentzian. For Normal, similar.
    
    noise_D = 0.1 # Low noise environment
    
    k_values = np.linspace(0, 5, 20)
    r_means = []
    
    theta = np.random.uniform(0, 2*np.pi, N)
    
    for K in k_values:
        # Annealing: Keep previous theta to settle faster? 
        # Or reset to avoid history? Let's reset for pure phase transition curve.
        theta = np.random.uniform(0, 2*np.pi, N) 
        
        r_history = []
        # Transient
        for _ in range(1000):
            theta = kuramoto_step(theta, omega, K, noise_D, DT)
            
        # Sampling
        for _ in range(1000):
            theta = kuramoto_step(theta, omega, K, noise_D, DT)
            r = calc_order_parameter(theta)
            r_history.append(r)
            
        r_means.append(np.mean(r_history))
        print(f"   K={K:.2f}, <r>={r_means[-1]:.3f}")
        
    return k_values, r_means

def plot_results(k_vals, r_vals):
    plt.figure(figsize=(10, 6))
    plt.plot(k_vals, r_vals, 'o-', color='purple', linewidth=2)
    plt.xlabel('Coupling Strength $K$ (Empatia/Atenção)')
    plt.ylabel('Order Parameter $<r>$ (Nível de Consciência)')
    plt.title('Phase Transition of Consciousness (Kuramoto Model)')
    plt.grid(True, alpha=0.3)
    plt.axhline(0.5, linestyle='--', color='gray', alpha=0.5, label='Transition Threshold')
    
    # Annotation
    plt.text(0.5, 0.1, 'Incoherent Phase\n(Unconscious)', fontsize=12, color='gray')
    plt.text(3.5, 0.9, 'Synchronized Phase\n(Conscious)', fontsize=12, color='purple')
    
    output_path = os.path.join(OUTPUT_DIR, 'consciousness_phase_transition.png')
    plt.savefig(output_path)
    print(f"[RESULT] Plot saved to: {output_path}")

if __name__ == "__main__":
    print("=== Thermodynamics of Consciousness Simulation ===")
    
    k_v, r_v = run_phase_transition_experiment()
    plot_results(k_v, r_v)
