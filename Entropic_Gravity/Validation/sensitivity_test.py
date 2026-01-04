"""
Sensitivity Analysis Module
---------------------------
Checks the robustness of the Entropic Gravity model against parameter variations.

Objective:
Ensure that the "Flat Rotation Curve" result is not fine-tuned to a specific
value of a0 (Verlinde's constant). The physics should hold even if a0 varies
by ±20-30%.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add src to path to import galactic_rotation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

try:
    from galactic_rotation import stable_orbital_velocity, A_0
except ImportError:
    # Fallback if running from a different directory structure
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
    from galactic_rotation import stable_orbital_velocity, A_0

def run_sensitivity_test():
    print("RUNNING PARAMETER SENSITIVITY ANALYSIS...")
    
    # Define variations of a0
    variations = [0.7, 0.8, 1.0, 1.2, 1.3] # -30% to +30%
    colors = ['r--', 'r-', 'k-', 'b-', 'b--']
    labels = ['-30%', '-20%', 'Baseline', '+20%', '+30%']
    
    radii = np.linspace(10, 100, 50)
    
    plt.figure(figsize=(10, 6))
    
    results = []
    
    for i, factor in enumerate(variations):
        a0_varied = A_0 * factor
        
        # We need to temporarily patch/use the varied A_0.
        # Since A_0 is a global in galactic_rotation, we might need to modify how we call it
        # or just reimplement the simple logic here for the test to avoid monkeypatching complex globals.
        # But `stable_orbital_velocity` calls `verlinde_force` which uses `A_0`.
        # To strictly test the logic, we can monkeypatch.
        
        import galactic_rotation
        galactic_rotation.A_0 = a0_varied
        
        # Calculate curve
        velocities = [galactic_rotation.stable_orbital_velocity(r, 'verlinde') for r in radii]
        results.append(velocities)
        
        plt.plot(radii, velocities, colors[i], linewidth=2 if factor == 1.0 else 1, label=f'a0 {labels[i]}')
        
    # Restore A_0
    galactic_rotation.A_0 = A_0
    
    plt.title('Sensitivity Analysis: Variation of Universal Acceleration a0')
    plt.xlabel('Distance')
    plt.ylabel('Orbital Velocity')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('sensitivity_analysis.png')
    print("[SAVED] Sensitivity Plot Saved: sensitivity_analysis.png")
    
    # Check robustness
    # The curve should remain roughly flat (low variance) even if amplitude changes
    variances = []
    print("\nRobustness Check (Flatness):")
    for i, velocities in enumerate(results):
        # Calculate coefficient of variation for the outer part (flat region)
        outer_vels = velocities[25:] # Last half
        variation = np.std(outer_vels) / np.mean(outer_vels)
        variances.append(variation)
        print(f"  a0 {labels[i]}: Variation = {variation:.2%}")
        
    max_var = max(variances)
    
    # Report
    with open("sensitivity_report.md", "w", encoding='utf-8') as f:
        f.write("# Sensitivity Analysis Report\n\n")
        f.write("## Objective\n")
        f.write("Evaluate if the flat rotation curve is a fine-tuned result or a robust feature.\n\n")
        f.write("## Results\n")
        f.write(f"Tested variations of `a_0`: -30% to +30%\n\n")
        f.write("| Variation | Flatness Error (CoV) | Status |\n")
        f.write("| :--- | :--- | :--- |\n")
        
        for i, var in enumerate(variances):
            status = "Stable" if var < 0.10 else "Unstable"
            f.write(f"| {labels[i]} | {var:.2%} | {status} |\n")
            
        f.write(f"\n**Conclusion:** Maximum variation in flatness is {max_var:.2%}.\n")
        if max_var < 0.15:
             f.write("[SUCCESS] **ROBUST.** The qualitative feature (flatness) persists across parameter variations.\n")
        else:
             f.write("[WARNING] **SENSITIVE.** The model requires precise tuning.\n")

if __name__ == "__main__":
    run_sensitivity_test()
