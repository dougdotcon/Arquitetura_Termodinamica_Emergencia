import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# CONFIGURAÇÃO DA MATRIZ SOCIAL
N = 20  # Tamanho otimizado para simulações rápidas (20x20 indivíduos)
J = 1.0  # Força da interação entre vizinhos (Influência social natural)

def inicializar_spins(N):
    """Inicializa spins aleatoriamente"""
    return np.random.choice([-1, 1], size=(N, N))

def passo_metropolis(spins, T, H_externo, passos_por_sweep=1):
    """
    Algoritmo de Monte Carlo para simular a evolução da sociedade.
    Retorna spins atualizados e energia média.
    """
    energia_total = 0
    magnetizacao_total = 0

    for _ in range(passos_por_sweep * N * N):
        i, j = np.random.randint(0, N), np.random.randint(0, N)
        s = spins[i, j]

        # Cálculo da energia local
        vizinhos = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N]
        dE = 2 * s * (J * vizinhos + H_externo)

        if dE < 0 or np.random.rand() < np.exp(-dE / T):
            spins[i, j] *= -1

    # Calcular energia e magnetização após equilíbrio
    energia = 0
    magnetizacao = np.sum(spins)
    for i in range(N):
        for j in range(N):
            vizinhos = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N]
            energia -= J * spins[i, j] * vizinhos + H_externo * spins[i, j]

    return spins, energia / (N*N), magnetizacao / (N*N)

def simular_transicao_fase(T_range, H_range, sweeps_equilibrio=20, sweeps_medida=10):
    """
    Simula a transição de fase variando temperatura e campo externo.
    Retorna magnetização, energia, susceptibilidade e calor específico.
    """
    magnetizacoes = np.zeros((len(T_range), len(H_range)))
    energias = np.zeros((len(T_range), len(H_range)))
    susceptibilidades = np.zeros((len(T_range), len(H_range)))
    calores_especificos = np.zeros((len(T_range), len(H_range)))

    for i, T in enumerate(tqdm(T_range, desc="Variação de Temperatura")):
        for j, H in enumerate(H_range):
            spins = inicializar_spins(N)

            # Equilibrar sistema
            for _ in range(sweeps_equilibrio):
                spins, _, _ = passo_metropolis(spins, T, H)

            # Medir propriedades
            energia_quadrado = 0
            magnetizacao_quadrado = 0
            energia_media = 0
            magnetizacao_media = 0

            for _ in range(sweeps_medida):
                spins, energia, magnetizacao = passo_metropolis(spins, T, H)
                energia_media += energia
                magnetizacao_media += magnetizacao
                energia_quadrado += energia**2
                magnetizacao_quadrado += magnetizacao**2

            energia_media /= sweeps_medida
            magnetizacao_media /= sweeps_medida
            energia_quadrado /= sweeps_medida
            magnetizacao_quadrado /= sweeps_medida

            magnetizacoes[i, j] = np.abs(magnetizacao_media)
            energias[i, j] = energia_media
            susceptibilidades[i, j] = (magnetizacao_quadrado - magnetizacao_media**2) / T
            calores_especificos[i, j] = (energia_quadrado - energia_media**2) / (T**2)

    return magnetizacoes, energias, susceptibilidades, calores_especificos

# Parâmetros da simulação
T_range = np.linspace(1.5, 3.5, 20)  # Temperaturas sociais
H_range = np.linspace(0.0, 2.0, 20)  # Campos externos (manipulação)

print("Iniciando simulações científicas do Horizonte de Eventos Social...")

# Executar simulações
mag, energia, suscep, calor = simular_transicao_fase(T_range, H_range)

# Salvar dados
np.savez('dados_simulacao.npz',
         temperaturas=T_range,
         campos=H_range,
         magnetizacao=mag,
         energia=energia,
         susceptibilidade=suscep,
         calor_especifico=calor)

print("Dados salvos em 'dados_simulacao.npz'")

# Criar visualizações
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Magnetização vs T para diferentes H
for j, H in enumerate([0, 5, 10, 15]):
    axes[0,0].plot(T_range, mag[:, j], label=f'H={H_range[j]:.1f}', marker='o', markersize=3)

axes[0,0].set_xlabel('Temperatura Social (T)')
axes[0,0].set_ylabel('Magnetização |M|')
axes[0,0].set_title('Transição de Fase Social')
axes[0,0].legend()
axes[0,0].grid(True)

# Susceptibilidade vs T
for j, H in enumerate([0, 5, 10, 15]):
    axes[0,1].plot(T_range, suscep[:, j], label=f'H={H_range[j]:.1f}', marker='s', markersize=3)

axes[0,1].set_xlabel('Temperatura Social (T)')
axes[0,1].set_ylabel('Susceptibilidade χ')
axes[0,1].set_title('Susceptibilidade Magnética')
axes[0,1].legend()
axes[0,1].grid(True)

# Magnetização vs H para diferentes T
for i, T in enumerate([2.0, 2.5, 3.0]):
    axes[1,0].plot(H_range, mag[i, :], label=f'T={T_range[i]:.1f}', marker='^', markersize=3)

axes[1,0].set_xlabel('Campo Externo (Manipulação H)')
axes[1,0].set_ylabel('Magnetização |M|')
axes[1,0].set_title('Efeito da Manipulação')
axes[1,0].legend()
axes[1,0].grid(True)

# Mapa de calor da magnetização
im = axes[1,1].imshow(mag, extent=[H_range[0], H_range[-1], T_range[0], T_range[-1]],
                      origin='lower', aspect='auto', cmap='viridis')
axes[1,1].set_xlabel('Campo Externo (H)')
axes[1,1].set_ylabel('Temperatura Social (T)')
axes[1,1].set_title('Mapa de Fase Social')
plt.colorbar(im, ax=axes[1,1], label='Magnetização |M|')

plt.tight_layout()
plt.savefig('analise_fase_social.png', dpi=150, bbox_inches='tight')
plt.show()

print("Análise completa salva em 'analise_fase_social.png'")
print("Projeto concluído com dados científicos robustos!")