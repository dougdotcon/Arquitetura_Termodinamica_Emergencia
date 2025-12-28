# IdeologicalEventHorizon

## Project Overview

**IdeologicalEventHorizon** is a computational sociology project that bridges statistical physics and social dynamics. It utilizes the **2D Ising Model** to simulate how institutional manipulation—represented by an external magnetic field—can induce critical phase transitions in a population. The project aims to demonstrate the existence of an "Ideological Event Horizon," a theoretical point of no return where deterministic forces overwhelm individual agency, leading to a rigid consensus.

## Key Scientific Findings

Based on extensive Monte Carlo simulations of a 20x20 lattice representing a social network:

- **Critical Point**: The system exhibits a critical temperature of `T_c ≈ 2.27`, mirroring the physical Ising model's phase transition.
- **Phase Transition**: The society shifts from a chaotic state with divided opinions (`|M| ≈ 0`) to an ordered state of total consensus (`|M| ≈ 1`).
- **Irreversibility**: External fields (manipulation) exceeding `H > 0.5` demonstrate the potential for irreversible institutional control.
- **Susceptibility**: Maximum social susceptibility (`χ_max ≈ 15-20`) occurs at the critical point, indicating high vulnerability to influence.

## Visualizations

![Social Phase Analysis](results/analise_fase_social.png)
*A comprehensive phase map displaying magnetization, susceptibility, and specific heat as functions of temperature and external field.*

![Manipulation Effect](results/efeito_manipulacao.png)
*Visualization of how external fields (institutional manipulation) drive the collapse of free will into deterministic alignment.*

## Scientific Objectives

1.  **Demonstrate the Social Event Horizon**: Mathematically prove the existence of a critical threshold where manipulation becomes irreversible.
2.  **Model Collective Phase Transitions**: Simulate phenomena such as collective hysteria, market crashes, and revolutionary shifts.
3.  **Bridge Micro-Macro Dynamics**: Connect individual behavioral changes to emergent, macroscopic social states.
4.  **Predict Social Anomalies**: Identify vulnerabilities within societies under stress.

## Methodology

### The Ising Model in Sociology

The simulation maps physical concepts to social dynamics:

*   **Spin (State)**: Represents an individual's opinion or sentiment (`+1` or `-1`).
*   **Interaction (Coupling J)**: The influence of peers and neighbors on an individual.
*   **Temperature (T)**: Represents social noise, chaos, or individual entropy.
*   **External Field (H)**: Represents institutional pressure or manipulation forcing alignment.

### Monte Carlo Algorithm

We employ the **Metropolis-Hastings algorithm** to simulate the probabilistic evolution of the social lattice:

1.  **Select**: Randomly choose an individual (spin).
2.  **Calculate**: Compute the change in social energy based on neighbor interactions and external influence.
3.  **Accept/Reject**: Flip the spin with a probability based on the Boltzmann distribution `exp(-ΔE / T)`.
4.  **Iterate**: Repeat for a defined number of steps until the system reaches equilibrium.

## Project Structure

```
IdeologicalEventHorizon/
├── README.md                    # Project documentation (this file)
├── requirements.txt             # Python dependencies
├── src/
│   └── ising_social_simulation.py  # Core simulation logic
├── data/
│   └── simulation_data.npz      # Raw simulation datasets
├── results/
│   ├── social_phase_analysis.png  # Phase diagram (M, χ, C vs T, H)
│   └── manipulation_effect.png    # Hysteresis and control plots
└── docs/
│   └── scientific_report.md     # Mathematical proofs and theory
```

## Installation & Usage

### Prerequisites

- Python 3.8+
- `numpy`, `matplotlib`

### Setup

```bash
pip install -r requirements.txt
```

### Running the Simulation

To generate the phase diagram and simulation data:

```bash
python src/ising_social_simulation.py
```

## Theory & Interpretation

This project treats society as a thermodynamic system. 
- **High Temperature**: High individual liberty and chaos; opinions fluctuate randomly.
- **Low Temperature**: High order and conformity; opinions are locked in.
- **Criticality**: The boundary between freedom and determinism.

By manipulating the external field `H`, we simulate how sustained propaganda or institutional pressure can lower the "energy cost" of conformity until the system snaps into a deterministic state.