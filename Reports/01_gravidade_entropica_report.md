# Relatório Técnico 01: Gravidade Entrópica e Curvas de Rotação Galáctica

**Data:** 27 de dezembro de 2025
**Autor:** Douglas Henrique Machado Fulber
**Contexto:** Verificação da Hipótese de Gravidade Emergente (Verlinde) vs Matéria Escura.

---

## 1. Fundamentação Teórica

O problema central da astrofísica moderna é que a matéria visível (bárions) nas galáxias não é suficiente para explicar as velocidades orbitais observadas nas bordas.

### 1.1 Modelo Newtoniano (Clássico)
Pela terceira lei de Kepler e mecânica newtoniana, a velocidade orbital $v$ de uma estrela a uma distância $r$ de um núcleo galáctico de massa $M(r)$ é dada por:

$$ \frac{v^2}{r} = \frac{G M(r)}{r^2} \implies v(r) = \sqrt{\frac{G M(r)}{r}} $$

Para regiões externas onde $M(r) \approx M_{total}$ (constante), esperamos o decaimento kepleriano:
$$ v(r) \propto \frac{1}{\sqrt{r}} $$

**Contradição Observacional:** As curvas reais são planas ($v \approx const$) para grandes $r$. A solução "padrão" é postular um halo de Matéria Escura $M_{DM}(r) \propto r$.

### 1.2 A Proposta Entrópica (Verlinde / MOND)
Erik Verlinde (2011) propõe que a gravidade é uma força entrópica emergente da tendência do universo maximizar a entropia nas telas holográficas. Em escalas cosmológicas (baixa aceleração), a entropia de emaranhamento modifica a lei de gravidade.

No regime de acelerações muito baixas ($a < a_0 \approx 1.2 \times 10^{-10} m/s^2$), a relação entre a aceleração gravitacional observada $a$ e a newtoniana $a_N$ muda. Isso é fenomenologicamente equivalente à MOND (Modified Newtonian Dynamics).

**Equação Governante (Interpolação):**
Usaremos a função de interpolação simples para estabilidade numérica:

$$ a = a_N \cdot \nu\left(\frac{a_N}{a_0}\right) $$

Onde a função de interpolação $\nu(y)$ (com $y = a_N/a_0$) satisfaz:
*   Para $y \gg 1$ (Newton): $\nu(y) \to 1$
*   Para $y \ll 1$ (Profundo MOND/Verlinde): $\nu(y) \to \frac{1}{\sqrt{y}}$

Uma escolha comum e robusta é:
$$ \nu(y) = \left( \frac{1}{1 + e^{-\sqrt{y}}} \right) \text{ ... (Simplificação Numérica) ou a forma padrão MOND: } \frac{1}{\sqrt{2}} \sqrt{1 + \sqrt{1 + 4y^{-2}}} $$

Para nossa simulação, usaremos a "Simple Interpolation Function" que inverte a relação $a \mu(a/a_0) = a_N$:
$$ \mu(x) = \frac{x}{1+x} \implies a = \frac{a_N}{2} + \sqrt{\frac{a_N^2}{4} + a_N a_0} $$
Isso garante uma transição suave.

---

## 2. Estratégia Numérica

### 2.1 O Integrador Simplético: Velocity Verlet
Para garantir a conservação de energia (no regime newtoniano) e estabilidade a longo prazo, evitaremos Euler ou Runge-Kutta 4 (que não é simplético).

**Algoritmo:**
1.  $\vec{r}(t+\Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + 0.5 \vec{a}(t) \Delta t^2$
2.  Calcular $\vec{a}(t+\Delta t)$ usando as novas posições.
3.  $\vec{v}(t+\Delta t) = \vec{v}(t) + 0.5 (\vec{a}(t) + \vec{a}(t+\Delta t)) \Delta t$

### 2.2 Implementação Computacional (Vetorizada)
Utilizaremos `numpy` para calcular as forças matricialmente ($N \times N$) sem loops Python lentos.
*   **Massas:** Núcleo galáctico massivo (fixo ou móvel) + disco de estrelas (massas de teste ou auto-gravitantes). Para ver o efeito puro na curva de rotação, modelaremos um potencial central dominante + correções 'Mean Field' se necessário, mas o foco inicial é a resposta da estrela ao campo central modificado.

### 2.3 Unidades Naturais de Simulação
*   $G = 1$
*   $M_{galaxy} = 1000$
*   $a_0 = 10^{-5}$ (Ajustado para que o raio da galáxia caia na transição).

---

## 3. Hipótese a Validar
Se o modelo estiver correto, ao plotar $v$ vs $r$:
1.  **Simulação Newtoniana:** A curva cairá.
2.  **Simulação Entrópica:** A curva permanecerá plana nas bordas, sem adicionar massa extra.

Próximo passo: Execução do script `simulacao_galaxia.py`.

---

## 4. Resultados da Simulação

A simulação computacional N-Body foi executada com sucesso. Abaixo apresentamos os resultados comparativos.

### 4.1 Gráfico de Velocidade Orbital vs Distância Radial
![Curva de Rotação](../Gravidade_Entropica/results/rotation_curve_comparison.png)

### 4.2 Interpretação Física
1. **Regime Newtoniano (Preto):** Observamos o decaimento kepleriano previsível ($v \propto r^{-1/2}$). Isso falha em representar galáxias reais, que possuem curvas planas.
2. **Regime Entrópico (Vermelho):** Com a correção de Verlinde/MOND ($a_0 = 10^{-3}$), a velocidade orbital nas bordas externas se estabiliza (flat rotation curve).
3. **Conclusão:** O efeito é reproduzido **sem adicionar massa extra** (Matéria Escura). A modificação na lei da gravidade em baixas acelerações é suficiente para sustentar as velocidades observadas.

O código fonte da simulação está disponível em `Gravidade_Entropica/src/simulacao_galaxia.py`.

