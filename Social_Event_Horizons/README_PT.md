# HorizonteIdeologicoEventos

## Visão Geral

O **HorizonteIdeologicoEventos** é um projeto de sociologia computacional que conecta a física estatística às dinâmicas sociais. Ele utiliza o **Modelo de Ising 2D** para simular como a manipulação institucional—representada por um campo magnético externo—pode induzir transições de fase críticas em uma população. O objetivo é demonstrar a existência de um "Horizonte de Eventos Ideológico", um ponto teórico de não retorno onde forças deterministas anulam a agência individual, resultando em um consenso rígido.

## Descobertas Científicas Principais

Com base em extensas simulações Monte Carlo utilizando uma malha 20x20 que representa uma rede social:

- **Ponto Crítico**: O sistema exibe uma temperatura crítica de `T_c ≈ 2.27`, espelhando a transição de fase do modelo Ising físico.
- **Transição de Fase**: A sociedade muda de um estado caótico com opiniões divididas (`|M| ≈ 0`) para um estado ordenado de consenso total (`|M| ≈ 1`).
- **Irreversibilidade**: Campos externos (manipulação) superiores a `H > 0.5` demonstram o potencial para controle institucional irreversível.
- **Susceptibilidade**: A susceptibilidade social máxima (`χ_max ≈ 15-20`) ocorre no ponto crítico, indicando alta vulnerabilidade à influência.

## Metodologia

### O Modelo Ising Aplicado à Sociologia

A simulação mapeia conceitos físicos para dinâmicas sociais:

*   **Spin (Estado)**: Representa a opinião ou sentimento de um indivíduo (`+1` ou `-1`).
*   **Interação (Acoplamento J)**: A influência de pares e vizinhos sobre um indivíduo.
*   **Temperatura (T)**: Representa o "ruído" social, o caos ou a entropia individual.
*   **Campo Externo (H)**: Representa a pressão institucional ou manipulação que força o alinhamento.

### Algoritmo de Monte Carlo

Utilizamos o **algoritmo Metropolis-Hastings** para simular a evolução probabilística da malha social:

1.  **Selecionar**: Escolher aleatoriamente um indivíduo (spin).
2.  **Calcular**: Calcular a variação na energia social baseada nas interações de vizinhos e influência externa.
3.  **Aceitar/Rejeitar**: Inverter o spin com uma probabilidade baseada na distribuição de Boltzmann `exp(-ΔE / T)`.
4.  **Iterar**: Repetir até que o sistema atinja o equilíbrio.

## Estrutura do Projeto


HorizonteIdeologicoEventos/
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências Python
├── src/
│   └── ising_social_simulation.py  # Lógica central da simulação
├── data/
│   └── simulation_data.npz      # Dados brutos das simulações
├── results/
│   ├── social_phase_analysis.png  # Diagrama de fase (M, χ, C vs T, H)
│   └── manipulation_effect.png    # Gráficos de histerese e controle
└── docs/
    └── theoretical_basis.pdf    # Provas matemáticas e teoria


## Instalação e Uso

### Pré-requisitos

- Python 3.8+
- `numpy`, `matplotlib`

### Configuração

bash
pip install -r requirements.txt


### Executando a Simulação

Para gerar o diagrama de fase e os dados de simulação:

bash
python src/ising_social_simulation.py


## Interpretação Teórica

Este projeto trata a sociedade como um sistema termodinâmico.
- **Alta Temperatura**: Alta liberdade individual e caos; opiniões flutuam aleatoriamente.
- **Baixa Temperatura**: Alta ordem e conformidade; opiniões são bloqueadas.
- **Criticidade**: O limite entre liberdade e determinismo.

Ao manipular o campo externo `H`, simulamos como a propaganda sustentada ou a pressão institucional pode reduzir o "custo de energia" da conformidade até que o sistema entre em colapso em um estado determinista.