# Technical Report 04: Information Causality and Transfer Entropy

**Date:** December 27, 2025
**Author:** Douglas Henrique Machado Fulber
**Context:** Definition of rigorous metrics to quantify information exchange ("Empathy") between complex systems, surpassing linear correlation.

---

## 1. The Correlation Problem

In conventional science, **Pearson Correlation** ($r$) is used to measure synchrony. However, correlation does not imply causality and is symmetric: $r(X, Y) = r(Y, X)$.

If a charismatic leader (X) influences the crowd (Y), correlation only says they move together. It fails to capture **who influences whom**.

## 2. Theoretical Foundation: Transfer Entropy

To physically prove "influence" or "interbrain coupling", we need to measure directed information flow. We use Schreiber's **Transfer Entropy (T)**.

Transfer Entropy $T_{X \to Y}$ measures the reduction of uncertainty about the future of $Y$ given knowledge of the past of $X$, beyond what is already known from the past of $Y$ itself.

$$ T_{X \to Y} = H(Y_{future} | Y_{past}) - H(Y_{future} | Y_{past}, X_{past}) $$

Formally (using Shannon Probabilities):

$$ T_{X \to Y} = \sum p(y_{t+1}, y_t, x_t) \log \left( \frac{p(y_{t+1} | y_t, x_t)}{p(y_{t+1} | y_t)} \right) $$

### 2.1 Interpretation
*   If $T_{X \to Y} > 0$: The past of $X$ improves the prediction of $Y$. There is information flow.
*   If $T_{X \to Y} \approx 0$: $X$ has no causal influence on $Y$.
*   **Asymmetry:** Generally $T_{X \to Y} \neq T_{Y \to X}$. This allows distinguishing the "Sender" (Leader/Therapist) from the "Receiver" (Patient/Crowd).

---

## 3. Numerical Strategy

We will implement a discrete estimator (histogram-based) to calculate $T_{X \to Y}$ and $T_{Y \to X}$ on synthetic time series.

### 3.1 Data Generation (Unidirectional Coupling)
We will simulate two coupled autoregressive processes:
1.  **Process X (Source):** $x_{t+1} = 0.5 x_t + \eta_x$
2.  **Process Y (Destination):** $y_{t+1} = 0.5 y_t + C \cdot x_t + \eta_y$

Where $C$ is the coupling strength.

### 3.2 Validation Hypothesis
When applying the algorithm:
1.  The cross-correlation will be high for both.
2.  The Transfer Entropy $T_{X \to Y}$ will be high and proportional to $C$.
3.  The Transfer Entropy $T_{Y \to X}$ (inverse direction) will be close to zero.

This proves we can mathematically measure "empathy" as a physical channel of bits, distinguishing it from mere coincidence.

---

## 4. Analysis Results

We generated two time series $X$ (Source) and $Y$ (Destination) with directional coupling $X \to Y$.

### 4.1 Transfer Entropy Graph
![Transfer Entropy](../Acoplamento_Intercerebral/results/transfer_entropy_result.png)

### 4.2 Quantitative Interpretation
The numerical results obtained were:
*   $T_{X \to Y} \approx 0.3591$ bits
*   $T_{Y \to X} \approx 0.0273$ bits

**Scientific Conclusion:**
The Shannon metric correctly detected the direction of causality ("who influences whom").
1.  The high value of $T_{X \to Y}$ indicates that knowledge of $X$ significantly reduces uncertainty about the future of $Y$.
2.  The near-zero value of $T_{Y \to X}$ confirms that $Y$ does not influence $X$ (the follower does not pilot the leader).

This validates the tool necessary to measure "Interbrain Coupling" in real EEG data, distinguishing real Empathy from mere accidental synchrony.
