"""
Transfer Entropy Analysis (Information Flow)
--------------------------------------------
Author: Antigravity (AI Theoretical Physicist)
Date: 2025-12-27

Objective:
Demonstrate the capability to measure directed information flow (Causality)
between two coupled time series using Transfer Entropy, surpassing standard correlation.

Method:
- Generate synthetic data: Master (X) -> Slave (Y).
- Discretize continuous data into bins.
- Compute joint and conditional probabilities.
- Calculate Transfer Entropy T(X->Y) and T(Y->X).
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = r"C:\Users\Douglas\Desktop\Entropy\Acoplamento_Intercerebral\results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_coupled_series(n_points=10000, coupling=0.5):
    """
    Generate two autoregressive processes where X drives Y.
    x(t) = 0.6*x(t-1) + noise
    y(t) = 0.6*y(t-1) + coupling*x(t-1) + noise
    """
    x = np.zeros(n_points)
    y = np.zeros(n_points)
    
    # Pre-generate noise for speed
    noise_x = np.random.normal(0, 1, n_points)
    noise_y = np.random.normal(0, 1, n_points)
    
    for t in range(1, n_points):
        x[t] = 0.6 * x[t-1] + noise_x[t]
        y[t] = 0.6 * y[t-1] + coupling * x[t-1] + noise_y[t]
        
    return x, y

def compute_transfer_entropy(source, target, bins=10, lag=1):
    """
    Compute Transfer Entropy T(Source -> Target).
    TE = Sum p(y_next, y, x) * log( p(y_next | y, x) / p(y_next | y) )
    
    Simplified implementation using naive histogram binning.
    """
    # 1. Discretize data
    # Combine to find global range (or per series)
    s_min, s_max = source.min(), source.max()
    t_min, t_max = target.min(), target.max()
    
    # Digitize returns indices 1..bins
    s_disc = np.digitize(source, np.linspace(s_min, s_max, bins+1)) - 1
    t_disc = np.digitize(target, np.linspace(t_min, t_max, bins+1)) - 1
    
    # Clip to 0..bins-1
    s_disc = np.clip(s_disc, 0, bins-1)
    t_disc = np.clip(t_disc, 0, bins-1)
    
    # 2. Count Occurrences for probabilities
    # We need p(y_{t+1}, y_t, x_t)
    
    n = len(source)
    counts_cond3 = np.zeros((bins, bins, bins)) # p(y_next, y_now, x_now)
    counts_cond2 = np.zeros((bins, bins))       # p(y_next, y_now)
    counts_joint2 = np.zeros((bins, bins))      # p(y_now, x_now)
    counts_y1     = np.zeros(bins)              # p(y_now)
    
    # We loop from 'lag' to n-1
    # y_next = t_disc[i]
    # y_now  = t_disc[i-lag]
    # x_now  = s_disc[i-lag]
    
    eff_len = 0
    for i in range(lag, n):
        y_next = t_disc[i]
        y_now  = t_disc[i-lag]
        x_now  = s_disc[i-lag]
        
        counts_cond3[y_next, y_now, x_now] += 1
        
        # Marginal counts needed for TE formula
        # Actually TE = Sum p(y+, y, x) * log ( p(y+, y, x) * p(y) / (p(y, x) * p(y+, y)) )
        # A more stable form:
        # TE = H(y_next | y_now) - H(y_next | y_now, x_now)
        
        eff_len += 1
        
    # Normalize to probabilities
    p_yplus_y_x = counts_cond3 / eff_len
    
    # Marginalize to get lower order probs
    p_yplus_y = np.sum(p_yplus_y_x, axis=2) # sum over x
    p_y_x     = np.sum(p_yplus_y_x, axis=0) # sum over y_next
    p_y       = np.sum(p_y_x, axis=1)       # sum over x
    
    # Calculate Conditional Entropies
    # H(Y_next | Y) = - Sum p(y+, y) log p(y+|y) = - Sum p(y+, y) log (p(y+, y)/p(y))
    h_y_cond_y = 0.0
    for yn in range(bins):
        for y in range(bins):
            if p_yplus_y[yn, y] > 0 and p_y[y] > 0:
                h_y_cond_y -= p_yplus_y[yn, y] * np.log2(p_yplus_y[yn, y] / p_y[y])
                
    # H(Y_next | Y, X) = - Sum p(y+, y, x) log (p(y+, y, x) / p(y, x))
    h_y_cond_yx = 0.0
    for yn in range(bins):
        for y in range(bins):
            for x in range(bins):
                if p_yplus_y_x[yn, y, x] > 0 and p_y_x[y, x] > 0:
                    h_y_cond_yx -= p_yplus_y_x[yn, y, x] * np.log2(p_yplus_y_x[yn, y, x] / p_y_x[y, x])
                    
    te = h_y_cond_y - h_y_cond_yx
    return te

def analyze_coupling():
    print("[INFO] Generating Coupled Time Series (X -> Y)...")
    
    x, y = generate_coupled_series(coupling=0.8)
    
    # Plot section of timeseries
    plt.figure(figsize=(12, 4))
    plt.plot(x[:200], label='Source X (Líder)', alpha=0.8)
    plt.plot(y[:200], label='Target Y (Seguidor)', alpha=0.8)
    plt.title('Simulated EEG Signals (Coupled)')
    plt.legend()
    output_ts = os.path.join(OUTPUT_DIR, 'eeg_signals.png')
    plt.savefig(output_ts)
    print(f"[RESULT] Time series plot saved to: {output_ts}")
    
    print("[INFO] Computing Transfer Entropy...")
    
    # Forward: X -> Y
    te_xy = compute_transfer_entropy(x, y)
    print(f"   TE(X -> Y): {te_xy:.4f} bits (Expected High)")
    
    # Backward: Y -> X
    te_yx = compute_transfer_entropy(y, x)
    print(f"   TE(Y -> X): {te_yx:.4f} bits (Expected Low)")
    
    # Bar plot comparison
    plt.figure(figsize=(6, 5))
    dirs = ['X -> Y', 'Y -> X']
    vals = [te_xy, te_yx]
    colors = ['green', 'gray']
    
    plt.bar(dirs, vals, color=colors)
    plt.ylabel('Transfer Entropy (bits)')
    plt.title('Directional Information Flow Analysis')
    plt.grid(axis='y', alpha=0.3)
    
    output_te = os.path.join(OUTPUT_DIR, 'transfer_entropy_result.png')
    plt.savefig(output_te)
    print(f"[RESULT] TE Analysis saved to: {output_te}")

if __name__ == "__main__":
    analyze_coupling()
