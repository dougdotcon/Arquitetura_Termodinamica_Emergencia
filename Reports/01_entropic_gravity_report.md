# Technical Report 01: Entropic Gravity and Galactic Rotation Curves

**Date:** December 27, 2025
**Author:** Douglas Henrique Machado Fulber
**Context:** Verification of Emergent Gravity Hypothesis (Verlinde) vs Dark Matter.

---

## 1. Theoretical Foundation

The central problem of modern astrophysics is that visible matter (baryons) in galaxies is not sufficient to explain the orbital velocities observed at the edges.

### 1.1 Newtonian Model (Classical)
By Kepler's third law and Newtonian mechanics, the orbital velocity $v$ of a star at a distance $r$ from a galactic nucleus of mass $M(r)$ is given by:

$$ \frac{v^2}{r} = \frac{G M(r)}{r^2} \implies v(r) = \sqrt{\frac{G M(r)}{r}} $$

For outer regions where $M(r) \approx M_{total}$ (constant), we expect Keplerian decay:
$$ v(r) \propto \frac{1}{\sqrt{r}} $$

**Observational Contradiction:** Real curves are flat ($v \approx const$) for large $r$. The "standard" solution is to postulate a halo of Dark Matter $M_{DM}(r) \propto r$.

### 1.2 The Entropic Proposal (Verlinde / MOND)
Erik Verlinde (2011) proposes that gravity is an entropic force emergent from the universe's tendency to maximize entropy on holographic screens. At cosmological scales (low acceleration), entanglement entropy modifies the law of gravity.

In the regime of very low accelerations ($a < a_0 \approx 1.2 \times 10^{-10} m/s^2$), the relationship between the observed gravitational acceleration $a$ and the Newtonian one $a_N$ changes. This is phenomenologically equivalent to MOND (Modified Newtonian Dynamics).

**Governing Equation (Interpolation):**
We will use the simple interpolation function for numerical stability:

$$ a = a_N \cdot \nu\left(\frac{a_N}{a_0}\right) $$

Where the interpolation function $\nu(y)$ (with $y = a_N/a_0$) satisfies:
*   For $y \gg 1$ (Newton): $\nu(y) \to 1$
*   For $y \ll 1$ (Deep MOND/Verlinde): $\nu(y) \to \frac{1}{\sqrt{y}}$

A common and robust choice is:
$$ \nu(y) = \left( \frac{1}{1 + e^{-\sqrt{y}}} \right) \text{ ... (Numerical Simplification) or the standard MOND form: } \frac{1}{\sqrt{2}} \sqrt{1 + \sqrt{1 + 4y^{-2}}} $$

For our simulation, we will use the "Simple Interpolation Function" that inverts the relation $a \mu(a/a_0) = a_N$:
$$ \mu(x) = \frac{x}{1+x} \implies a = \frac{a_N}{2} + \sqrt{\frac{a_N^2}{4} + a_N a_0} $$
This ensures a smooth transition.

---

## 2. Numerical Strategy

### 2.1 The Symplectic Integrator: Velocity Verlet
To ensure energy conservation (in the Newtonian regime) and long-term stability, we will avoid Euler or Runge-Kutta 4 (which is not symplectic).

**Algorithm:**
1.  $\vec{r}(t+\Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + 0.5 \vec{a}(t) \Delta t^2$
2.  Calculate $\vec{a}(t+\Delta t)$ using the new positions.
3.  $\vec{v}(t+\Delta t) = \vec{v}(t) + 0.5 (\vec{a}(t) + \vec{a}(t+\Delta t)) \Delta t$

### 2.2 Computational Implementation (Vectorized)
We will use `numpy` to calculate forces matrix-wise ($N \times N$) without slow Python loops.
*   **Masses:** Massive galactic nucleus (fixed or mobile) + disk of stars (test masses or self-gravitating). To see the pure effect on the rotation curve, we will model a dominant central potential + 'Mean Field' corrections if necessary, but the initial focus is the star's response to the modified central field.

### 2.3 Natural Simulation Units
*   $G = 1$
*   $M_{galaxy} = 1000$
*   $a_0 = 10^{-5}$ (Adjusted so the galaxy radius falls in the transition).

---

## 3. Hypothesis to Validate
If the model is correct, when plotting $v$ vs $r$:
1.  **Newtonian Simulation:** The curve will drop.
2.  **Entropic Simulation:** The curve will remain flat at the edges, without adding extra mass.

Next step: Execution of script `simulacao_galaxia.py`.

---

## 4. Simulation Results

The N-Body computational simulation was successfully executed. Below we present the comparative results.

### 4.1 Orbital Velocity vs Radial Distance Graph
![Rotation Curve](../Gravidade_Entropica/results/rotation_curve_comparison.png)

### 4.2 Physical Interpretation
1. **Newtonian Regime (Black):** We observe predictable Keplerian decay ($v \propto r^{-1/2}$). This fails to represent real galaxies, which have flat curves.
2. **Entropic Regime (Red):** With the Verlinde/MOND correction ($a_0 = 10^{-3}$), the orbital velocity at the outer edges stabilizes (flat rotation curve).
3. **Conclusion:** The effect is reproduced **without adding extra mass** (Dark Matter). The modification in the law of gravity at low accelerations is sufficient to sustain the observed velocities.

The source code of the simulation is available at `Gravidade_Entropica/src/simulacao_galaxia.py`.
