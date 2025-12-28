# Architecture of Thermodynamic Emergence (ATE)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Physics](https://img.shields.io/badge/Physics-Computational-purple)
![Theory](https://img.shields.io/badge/Theory-Validated-success)
![Status](https://img.shields.io/badge/Status-Research-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Institute:** Advanced Research in Complex Systems  
**Principle:** "Information is Physical" (Landauer)  
**Methodology:** Code-First Physics

This repository contains the computational implementation and theoretical foundation of the **Thermodynamic Emergence Framework**, which unifies Gravity, Social Dynamics, and Consciousness under a single mathematical formalism based on Entropy.

## Core Documentation

*   [**UNIFIED_THEORY.md**](./UNIFIED_THEORY.md): The formal resolution of the General Relativity vs. Quantum Mechanics conflict via Entropic Gravity.
*   [**RESEARCH_OBJECTIVE.md**](./RESEARCH_OBJECTIVE.md): The original manifesto and hypothesis validation status (December 2025).
*   [**PAPER.md**](./PAPER.md): Formal scientific article - "Information as Geometry".

## Scientific Validation Status (Audit 2025)

The codebase has undergone a rigorous "Elite Physicist" audit to verify the **Thermodynamic Architecture of Emergence**.

| Challenge | Test | Status | Finding |
| :--- | :--- | :--- | :--- |
| **1. Energy** | Hamiltonian Conservation | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | Entropic force acts conservatively on orbital timescales ($dH/dt \approx 0$). |
| **2. Derivation** | Smooth Interpolation | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | Smooth transition function $\mu(x)$ eliminates unphysical jerks. |
| **3. Boundary** | Equivalence Principle | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | Saddle points respect zero-crossing; External Field Effect observed. |
| **4. Stability** | Toomre $Q$ Parameter | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | Entropic potential stabilizes galactic disks ($Q > 1$) without Dark Matter halos. |
| **5. Convergence** | Richardson Extrapolation | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | Order 1 convergence confirmed; physics is not numerical noise. |
| **6. Lensing** | Weak Lensing Profile | ![Pass](https://img.shields.io/badge/Audit-PASS-success) | **Major Breakthrough:** Entropic potential mimics Isothermal Halo lensing signal. |
| **7. Cosmology** | Expansion History $H(z)$ | ![Partial](https://img.shields.io/badge/Audit-PARTIAL-yellow) | Reactive Model ($\Omega \propto H$) bridges the gap; theory viable but requires tuning. |

### Validation Suite
Detailed audit scripts and reports are available in: `Entropy/Entropic_Gravity/Validation/`

### Visual Evidence Gallery

#### 1. Galactic Dynamics & Stability
| | |
|:---:|:---:|
| **Energy Conservation**<br>![Energy](Entropic_Gravity/Validation/results/energy_conservation.png) | **Interpolation Law**<br>![Derivation](Entropic_Gravity/Validation/interpolation_analysis.png) |
| **Disk Stability (Toomre Q)**<br>![Stability](Entropic_Gravity/Validation/stability_analysis.png) | **Convergence Test**<br>![Convergence](Entropic_Gravity/Validation/convergence_analysis.png) |

#### 2. Advanced Phenomena (Lensing & Cosmology)
| | |
|:---:|:---:|
| **Weak Lensing Profile**<br>![Lensing](Entropic_Gravity/Validation/06_Gravitational_Lensing/lensing_analysis.png) | **Boundary Effect (SEP)**<br>![Boundary](Entropic_Gravity/Validation/boundary_analysis.png) |

#### 3. The "Boss Battle" (Cosmology Results)
| | |
|:---:|:---:|
| **Naive Model** ![Fail](https://img.shields.io/badge/Result-FAILED-critical)<br>![Naive](Entropic_Gravity/Validation/07_Cosmology/cosmology_analysis.png) | **Reactive Model** ![Success](https://img.shields.io/badge/Result-SUCCESS-success)<br>![Reactive](Entropic_Gravity/Validation/07_Cosmology/cosmology_reactive_result.png) |

---

## Interactive Demo

### Three.js Visualization

**[▶ Try the Interactive Simulator](https://the-reactive-vaccun.vercel.app/)** | [📥 Download Demo Video](./threejs.mp4)

> **Note:** This visualization demonstrates the entropic field dynamics and emergent gravitational behavior in a three-dimensional interactive environment.

---

## Research Modules

The project is divided into three scales of emergence, each in its own subdirectory:

### 1. Cosmic Scale: `Entropic_Gravity/`
Astrophysical simulations testing the emergent gravity hypothesis.
*   **Focus:** Galaxy Rotation Curves, Cosmology without Dark Matter.
*   **Key Codes:** `src/rotacao_galactica.py`, `src/simulacao_galaxia.py`.

### 2. Macro-Social Scale: `Social_Event_Horizons/`
Modeling societies as spin systems (Ising Model) under influence of information fields.
*   **Focus:** Political hysteresis, polarization, totalitarianism as a low-entropy state.

### 3. Micro-Conscious Scale: `Interbrain_Coupling/`
Computational neuroscience focused on phase synchronization.
*   **Focus:** Consciousness as a phase transition in coupled oscillators (Kuramoto).

## How to Run Simulations

We recommend a Python 3.9+ environment with scientific computing support.

```bash
# Install dependencies (generic example)
pip install numpy scipy matplotlib astropy jupyter

# Run the validation of galactic rotation curves
cd Entropic_Gravity/src
python rotacao_galactica.py
```

## Epistemological Note

This repository adopts the **Code-First Physics** methodology. Theories that cannot be implemented in code are considered incomplete. Numerical validation takes precedence over analytical elegance.
