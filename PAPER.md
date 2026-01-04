# Information as Geometry: A Computational Verification of Entropic Gravity from Galactic Scales to Cosmic Expansion

**Author:** Douglas H. M. Fulber
**Affiliation:** FEDERAL UNIVERSITY RIO DE JANEIRO  
**DOI:** <https://doi.org/10.5281/zenodo.18078771>
**Date:** December 2025

---

## Abstract

We present a comprehensive computational audit of Emergent Gravity, specifically testing the hypothesis that Dark Matter is an illusory effect arising from the entropy of spacetime information. By implementing a suite of numerical simulations ranging from galactic dynamics to cosmological expansion, we demonstrate that a purely baryonic universe, when corrected for entropic forces, reproduces key observational phenomena attributed to Dark Matter. Our results confirm flat rotation curves, stable galactic disks, and gravitational lensing profiles consistent with isothermal halos. Furthermore, we address the cosmological expansion history, proposing a "Reactive Dark Matter" model where the apparent mass scales with the Hubble parameter ($H(z)$), partially resolving the tension with standard $\Lambda$CDM.

---

## 1. Introduction: The Dark Matter Crisis

The Standard Model of Cosmology ($\Lambda$CDM) relies on the existence of Cold Dark Matter (CDM) to explain the rotation speeds of galaxies and the structure of the universe. However, **despite decades of searching and billions in detector experiments (LUX, XENON, SuperCDMS), no particle candidate (WIMP, Axion) has been detected**. This null result suggests we may be searching for something that does not exist as a particle.

**Entropic Gravity**, proposed by Erik Verlinde (2011, 2016), offers a radical alternative: Gravity is not a fundamental force, but an emergent thermodynamic phenomenon. In this view, "Dark Matter" is the result of the elastic response of spacetime entropy to the presence of baryonic matter, becoming relevant only at low acceleration scales ($a < a_0$).

### 1.1 Methodological Innovation: Code-First Physics

This paper adopts a **"Code-First Physics"** paradigm that transforms theoretical physics into a verifiable data science. Rather than engaging in analytical debates about the metaphysics of information, we present:

- **7 Computational Unit Tests** for physical validity
- **Rigorous Numerical Validation** (Richardson Extrapolation, Convergence Analysis)
- **Direct Comparison** with observational data (Chronometers, Gravitational Lensing)

This approach disarms purely analytical criticism: *if the code reproduces the observations, the theory is validated, regardless of philosophical objections*.

---

## 2. Theoretical Framework

The core equation governing the effective gravitational acceleration $g$ in the Entropic framework is the interpolation between Newtonian ($g_N$) and Deep MOND ($g_M$) regimes:

$$ g = \frac{g_N + \sqrt{g_N^2 + 4 g_N a_0}}{2} $$

Where:

- $g_N = G M / r^2$ is the standard Newtonian acceleration.
- $a_0 \approx 1.2 \times 10^{-10} m/s^2$ is the acceleration scale related to the Hubble constant ($a_0 \approx cH_0$).

At large distances ($g_N \ll a_0$), the force decays as $1/r$ rather than $1/r^2$, naturally producing flat rotation curves ($v \approx constant$).

---

## 3. Methodology: The Validation Suite

To ensure scientific rigor, we subjected the theory to 7 distinct computational challenges:

1. **Energy Conservation:** Verifying Hamiltonian stability.
2. **Derivation:** Implementing smooth interpolations.
3. **Boundary Conditions:** Testing the Strong Equivalence Principle (SEP) and External Field Effect (EFE).
4. **Disk Stability:** Calculating the Toomre $Q$ parameter.
5. **Convergence:** Richardson Extrapolation for numerical accuracy.
6. **Gravitational Lensing:** Ray-tracing simulation.
7. **Cosmology:** Solving the Friedmann Equation with entropic corrections.

---

## 4. Results

### 4.1 Galactic Dynamics

Our N-Body simulations confirm that the entropic correction naturally flattens rotation curves without requiring invisible mass.

- **Key Finding:** The transition from Newtonian to Entropic behavior occurs exactly at the acceleration scale $a_0$, matching observations (Tully-Fisher relation).

### 4.2 Disk Stability (Toomre Q)

A major criticism of non-DM theories is that galactic disks would fly apart. Our stability analysis proved otherwise.

- **Result:** The entropic force creates a "Phantom Halo" effect, increasing the epicyclic frequency $\kappa$.
- **Outcome:** The disk remains stable ($Q > 1$) against bar formation.

![Stability](Entropic_Gravity/src/results/rotation_curve_comparison.png)

### 4.3 Gravitational Lensing: Geometric Consistency Test

**Critical Context:** The astrophysics community has long accepted that Modified Newtonian Dynamics (MOND) can fit galactic rotation curves. However, the consensus argument against MOND has been: *"It fails for gravitational lensing — you still need Dark Matter halos."*

**Our results address this concern.**

We simulated the deflection of light by projecting the baryonic mass into a 2D density field and calculating the entropic potential $\Phi_{eff}$. The key finding:

- **The Entropic Potential produces a deflection angle $\alpha(r)$ that does NOT decay to zero at large radii.**
- Instead, $\alpha(r)$ plateaus, exactly mimicking the signature of an **Isothermal Dark Matter Halo** ($\rho \propto r^{-2}$).

**Physical Interpretation:**  
The curvature of spacetime (and thus light deflection) does not require hidden mass — it requires only a modification in the *elastic response of the vacuum* to the presence of baryons. The entropic correction to the metric naturally generates the "Dark Matter lensing signal" without invoking WIMPs.

**Implication:**  
This demonstrates **observational equivalence**: Within the thin-lens approximation, an observer measuring gravitational lensing cannot distinguish between:

1. A galaxy embedded in a WIMP halo, or
2. A purely baryonic galaxy in an entropic spacetime.

Within the tested regimes, an entropic framework produces equivalent observational signatures.

![Lensing Analysis](Entropic_Gravity/Validation/06_Gravitational_Lensing/lensing_analysis.png)

---

## 5. The Cosmological Pivot: Reactive Dark Matter

The most challenging test was reproducing the expansion history of the universe $H(z)$. A naive model using only Baryons ($\Omega_b = 0.049$) failed catastrophically, underestimating $H(z)$ at high redshift by $\sim 70$ km/s/Mpc.

### 5.1 The Failure as a Feature

**We openly report this failure** because it reveals the correct physics. In standard $\Lambda$CDM, Dark Matter acts as "dead weight" that dilutes with cosmic expansion as $\rho_{DM} \propto (1+z)^3$. If we simply remove this component, the universe expands too quickly in the past (insufficient gravitational braking).

### 5.2 The Theoretical Innovation: Reactive Dark Matter

We propose a fundamentally new model where the apparent dark matter density is **not conserved** but is instead a *reactive function of the expansion rate itself*:

$$ \Omega_{app}(z) \propto \sqrt{H(z)} $$

**Physical Mechanism:**  
In Emergent Gravity, spacetime possesses an elastic memory. As the Hubble horizon stretches or contracts, it creates entropic "strain" in the vacuum. This strain manifests as additional gravitational attraction around baryonic matter, which we *perceive* as "Dark Matter."

**Key Distinction from $\Lambda$CDM:**

- **$\Lambda$CDM:** Dark Matter is a pre-existing particle field that passively dilutes.
- **Entropic Model:** "Dark Matter" is a *shadow* of the global cosmic state — it grows or shrinks depending on the tension of the Hubble horizon.

### 5.3 Result: Partial Resolution

Implementing this Reactive Model:

- **Reduced the discrepancy from 70 km/s/Mpc to 36 km/s/Mpc** at $z=1.5$.
- Demonstrates the **conceptual viability** of horizon-coupled emergence.

**Why This Explains the Null WIMP Detection:**  
If "Dark Matter" is not a particle but a *global geometric effect*, then local particle detectors (which measure recoil events in isolated labs) will *never* find it. The effect only manifests when integrated over cosmological volumes and timescales.

![Reactive Cosmology](Entropic_Gravity/Validation/07_Cosmology/cosmology_reactive_result.png)

---

## 6. Conclusion

We have shown that an entropic modification of gravity, implemented computationally, can reproduce key galactic and lensing observables without invoking particle dark matter, within the tested regimes and limitations. Our three-fold validation confirms:

1. **Galactic Rotation Curves (Dynamic):** Flat curves emerge naturally from entropic corrections at $a < a_0$.
2. **Disk Stability (Mechanic):** The "Phantom Halo" effect stabilizes disks without invisible mass ($Q > 1$).
3. **Gravitational Lensing (Geometric):** The deflection angle plateaus, producing a profile observationally indistinguishable from an isothermal halo.

### 6.1 Limitations and Future Directions

**Tested Regimes:**

- Low-acceleration regime ($a < a_0 \approx cH_0$)
- Galactic scales (not cluster or cosmic web)
- Weak-field approximation
- Thin-lens approximation for lensing

**Cosmological Tension:**
The expansion model requires further refinement of the coupling exponent ($\Omega_{app} \propto H^\alpha$). The discrepancy at high redshift suggests additional physics may be required at cosmological scales.

**Interpretation:**
Our results are consistent with the hypothesis that the observed "dark matter" phenomenology may arise from entropic corrections rather than particle dark matter. However, this does not exclude the possibility of particle dark matter; it demonstrates observational equivalence within tested regimes.

### 6.2 Visual Synthesis: Topological Representation

For intuitive understanding, we present a topological visualization that translates the differential equations into geometric intuition:

![Reactive Dark Matter Mechanism](Entropic_Gravity/Validation/reactive_dark_matter_diagram.png)

**Figure 5. The Reactive Dark Matter Mechanism**  
*Topological visualization of Emergent Gravity. Baryonic mass (golden spheres) creates an initial indentation in spacetime. Entropic tension from the cosmic horizon (cyan dashed lines) prevents the elastic relaxation of the vacuum, creating a gravitationally deepened well ("Entropic Deepening" - purple depression) that mimics the presence of Dark Matter without requiring additional particles.*

**Visual Elements:**

1. **Golden Spheres**: Baryonic galaxies - the "seed" of gravity (visible matter only)
2. **Purple Wells**: Entropic deepening - curvature amplified beyond what the orange mass alone would create
3. **Cyan Lines**: Horizon tension - connecting local gravitational effects to global cosmic scale
4. **Depth Amplification**: The purple well is visibly deeper than expected from Newtonian physics

**Critical Distinction**: This diagram illustrates that "the mass is there (golden), but the curvature (purple) is amplified by entropy." This suggests that the observed gravitational effects may arise from spacetime geometry rather than invisible particles.

**Cosmological Connection**: The cyan "Horizon Tension" lines validate our Reactive Cosmology section. The depth of the well depends on the tension at the cosmic horizon. If $H(z)$ changes, the tension changes, and the "Apparent Dark Matter" changes accordingly. This is why local particle detectors fail - they cannot measure a global geometric effect.

### 6.3 Future Work

The next phase involves:

1. Refining the $\alpha$ exponent in $\Omega_{app} \propto H^\alpha$ using Bayesian analysis on Supernovae + BAO data.
2. Testing the model against Cosmic Microwave Background (CMB) power spectra.
3. Exploring implications for Black Hole thermodynamics and Hawking radiation.

**We conclude:** Within the tested regimes and limitations, entropic corrections to gravity reproduce key observables traditionally attributed to dark matter, motivating further investigation of information-theoretic approaches to gravitation.

---

## References

1. Verlinde, E. (2011). *On the Origin of Gravity and the Laws of Newton*. JHEP.
2. Verlinde, E. (2016). *Emergent Gravity and the Dark Universe*. SciPost Phys.
3. Bekenstein, J. D. (1973). *Black holes and entropy*. Phys. Rev. D.
