# Relatório Técnico 02: Termodinâmica Social e Transições de Fase

**Data:** 27 de dezembro de 2025
**Autor:** Douglas Henrique Machado Fulber
**Contexto:** Modelagem de dinâmicas de opinião e polarização usando Mecânica Estatística.

---

## 1. Fundamentação Teórica: O Modelo de Ising Social

A sociedade humana pode ser modelada como um sistema de spins interagentes, onde cada indivíduo $i$ possui uma opinião binária $s_i = \pm 1$ (Concordo/Discordo, Direita/Esquerda).

### 1.1 O Hamiltoniano Social
A "energia" (ou tensão social) do sistema é dada por:

$$ \mathcal{H} = -J \sum_{\langle i, j \rangle} s_i s_j - H \sum_{i} s_i $$

Onde:
*   $J > 0$: Constante de acoplamento social (**Empatia/Mimetismo**). Se $J$ é alto, os vizinhos tendem a copiar a opinião uns dos outros (Ferromagnetismo).
*   $H$: Campo externo (**Mídia/Propaganda/Ideologia Dominante**). Tende a alinhar todos os spins numa direção forçada.
*   $\langle i, j \rangle$: Soma sobre vizinhos na rede social.

### 1.2 Temperatura Social ($T$)
Em física, $T$ é vibração aleatória. Em sociologia, $T$ é o **Ruído de Informação**, **Stress** ou **Anomia**.
*   Alta $T$: Comportamento aleatório, caótico (Gás Social). Ninguém influencia ninguém.
*   Baixa $T$: Comportamento cristalizado. A opinião do vizinho dita a sua (Sólido Social).

### 1.3 Transição de Fase
Existe uma temperatura crítica $T_c$ (Temperatura de Curie Social).
*   Se $T < T_c$: Ocorre quebra espontânea de simetria. A sociedade "congela" em um consenso ($+1$ ou $-1$) mesmo sem campo externo ($H=0$).
*   Se $T > T_c$: A sociedade é desordenada (Magnetização $M \approx 0$).

---

## 2. Estratégia Numérica: Algoritmo de Metropolis

Para simular a evolução temporal das opiniões, usamos a dinâmica de Monte Carlo via algoritmo de Metropolis-Hastings.

### 2.1 Regra de Atualização
1.  Escolha um agente $i$ aleatoriamente.
2.  Calcule a variação de energia se ele inverter sua opinião ($s_i \to -s_i$):
    $$ \Delta E = 2 s_i \left( J \sum_{viz} s_{viz} + H \right) $$
3.  Critério de Aceitação:
    *   Se $\Delta E < 0$ (reduz tensão): Aceita a mudança.
    *   Se $\Delta E > 0$ (aumenta tensão): Aceita com probabilidade $P = e^{-\Delta E / k_B T}$.

Isso permite que o sistema escape de mínimos locais, mas tenda ao equilíbrio de Boltzmann.

### 2.2 Fenômeno de Histerese
Variaremos o campo externo $H$ de $-H_{max}$ até $+H_{max}$ e voltaremos. Em sistemas ferromagnéticos ($T < T_c$), a sociedade "lembra" do passado. Mesmo que a propaganda pare ($H=0$), a opinião pública continua polarizada na direção antiga. Isso demonstra a inércia social.

---

## 3. Implementação Computacional

*   **Grid:** Rede quadrada $50 \times 50$ (2500 agentes).
*   **Parâmetros de Controle:** $T$ (Social Temperature), $H$ (External Field).
*   **Observáveis:**
    *   Magnetização $M = \frac{1}{N} \sum s_i$ (Consenso).
    *   Suscetibilidade $\chi = \frac{\sigma_M^2}{T}$ (Volatilidade/Risco de Revolução).

O script `simulacao_social.py` gerará a curva de histerese e mapas de calor da opinião pública.

---

## 4. Resultados da Simulação

A simulação de Monte Carlo foi executada para $T=1.8$ (abaixo da temperatura crítica $T_c \approx 2.269$).

### 4.1 Histerese Social (Memória Coletiva)
![Histerese Social](../Horizontes_de_Eventos_Sociais/results/social_hysteresis_T1.8.png)

**Interpretação:**
A curva forma um ciclo aberto ("loop").
1.  **Trajetória Vermelha (Queda do Campo):** À medida que a propaganda diminui ($H$ vai de $+2$ para $-2$), a sociedade **resiste** à mudança. A magnetização permanece positiva (consenso antigo) mesmo quando $H$ cruza zero e se torna negativo.
2.  **Ponto de Ruptura:** A mudança de opinião só ocorre quando a pressão contrária atinge um limiar crítico (Revolução).
3.  **Conclusão Física:** A opinião pública possui "inércia". Uma vez polarizada, a sociedade não retorna ao estado neutro apenas removendo a causa da polarização. É necessária uma força contrária ativa e intensa para reverter o estado.

### 4.2 Snapshot da Sociedade Polarizada
![Snapshot da Rede](../Horizontes_de_Eventos_Sociais/results/social_snapshot_T1.8.png)

Agrupamentos (clusters) de opinião homogênea se formam espontaneamente (bolhas sociais).

