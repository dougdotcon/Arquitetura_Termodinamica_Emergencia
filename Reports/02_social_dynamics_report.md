# Technical Report 02: Social Thermodynamics and Phase Transitions

**Date:** December 27, 2025
**Author:** Douglas Henrique Machado Fulber
**Context:** Modeling opinion dynamics and polarization using Statistical Mechanics.

---

## 1. Theoretical Foundation: The Social Ising Model

Human society can be modeled as a system of interacting spins, where each individual $i$ has a binary opinion $s_i = \pm 1$ (Agree/Disagree, Right/Left).

### 1.1 The Social Hamiltonian
The "energy" (or social tension) of the system is given by:

$$ \mathcal{H} = -J \sum_{\langle i, j \rangle} s_i s_j - H \sum_{i} s_i $$

Where:
*   $J > 0$: Social coupling constant (**Empathy/Mimicry**). If $J$ is high, neighbors tend to copy each other's opinion (Ferromagnetism).
*   $H$: External field (**Media/Propaganda/Dominant Ideology**). Tends to align all spins in a forced direction.
*   $\langle i, j \rangle$: Sum over neighbors in the social network.

### 1.2 Social Temperature ($T$)
In physics, $T$ is random vibration. In sociology, $T$ is **Information Noise**, **Stress**, or **Anomie**.
*   High $T$: Random, chaotic behavior (Social Gas). No one influences anyone.
*   Low $T$: Crystallized behavior. The neighbor's opinion dictates yours (Social Solid).

### 1.3 Phase Transition
There exists a critical temperature $T_c$ (Social Curie Temperature).
*   If $T < T_c$: Spontaneous symmetry breaking occurs. Society "freezes" into a consensus ($+1$ or $-1$) even without an external field ($H=0$).
*   If $T > T_c$: Society is disordered (Magnetization $M \approx 0$).

---

## 2. Numerical Strategy: Metropolis Algorithm

To simulate the temporal evolution of opinions, we use Monte Carlo dynamics via the Metropolis-Hastings algorithm.

### 2.1 Update Rule
1.  Choose an agent $i$ randomly.
2.  Calculate the energy change if they flip their opinion ($s_i \to -s_i$):
    $$ \Delta E = 2 s_i \left( J \sum_{neigh} s_{neigh} + H \right) $$
3.  Acceptance Criterion:
    *   If $\Delta E < 0$ (reduces tension): Accept the change.
    *   If $\Delta E > 0$ (increases tension): Accept with probability $P = e^{-\Delta E / k_B T}$.

This allows the system to escape local minima but tend towards Boltzmann equilibrium.

### 2.2 Hysteresis Phenomenon
We will vary the external field $H$ from $-H_{max}$ to $+H_{max}$ and back. In ferromagnetic systems ($T < T_c$), society "remembers" the past. Even if propaganda stops ($H=0$), public opinion remains polarized in the old direction. This demonstrates social inertia.

---

## 3. Computational Implementation

*   **Grid:** Square lattice $50 \times 50$ (2500 agents).
*   **Control Parameters:** $T$ (Social Temperature), $H$ (External Field).
*   **Observables:**
    *   Magnetization $M = \frac{1}{N} \sum s_i$ (Consensus).
    *   Susceptibility $\chi = \frac{\sigma_M^2}{T}$ (Volatility/Risk of Revolution).

The script `simulacao_social.py` will generate the hysteresis curve and heatmaps of public opinion.

---

## 4. Simulation Results

The Monte Carlo simulation was executed for $T=1.8$ (below the critical temperature $T_c \approx 2.269$).

### 4.1 Social Hysteresis (Collective Memory)
![Social Hysteresis](../Horizontes_de_Eventos_Sociais/results/social_hysteresis_T1.8.png)

**Interpretation:**
The curve forms an open cycle ("loop").
1.  **Red Trajectory (Field Drop):** As propaganda decreases ($H$ goes from $+2$ to $-2$), society **resists** change. Magnetization remains positive (old consensus) even when $H$ crosses zero and becomes negative.
2.  **Break Point:** The change of opinion only occurs when the opposing pressure reaches a critical threshold (Revolution).
3.  **Physical Conclusion:** Public opinion has "inertia". Once polarized, society does not return to the neutral state just by removing the cause of polarization. An active and intense opposing force is needed to reverse the state.

### 4.2 Snapshot of Polarized Society
![Network Snapshot](../Horizontes_de_Eventos_Sociais/results/social_snapshot_T1.8.png)

Homogeneous opinion clusters form spontaneously (social bubbles).
