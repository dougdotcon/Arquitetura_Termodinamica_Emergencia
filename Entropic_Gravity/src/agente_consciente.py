"""
Módulo do Agente Consciente: Consciência como Anti-Gravidade

Este módulo implementa um agente consciente que pode prever entropia local
e tomar decisões para reduzir entropia, permitindo orbitar ou escapar
do buraco negro entrópico, enquanto matéria inerte cai.

Teoria: A consciência é a injeção de ordem que resiste à queda entrópica.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional

class AgenteConsciente:
    """
    Agente consciente que modela consciência como redução de entropia local.

    Atributos:
    - posicao: Tupla (x, y) da posição atual
    - velocidade: Tupla (vx, vy) da velocidade atual
    - horizonte_previsao: Número de passos para prever futuro
    - forca_consciente: Intensidade da força anti-gravidade
    """

    def __init__(self, posicao_inicial: Tuple[float, float] = (10.0, 0.0),
                 velocidade_inicial: Tuple[float, float] = (0.0, 1.0),
                 horizonte_previsao: int = 5,
                 forca_consciente: float = 0.1):
        """
        Inicializa o agente consciente.

        Parameters:
        -----------
        posicao_inicial : tuple
            Posição inicial (x, y)
        velocidade_inicial : tuple
            Velocidade inicial (vx, vy)
        horizonte_previsao : int
            Passos para prever entropia futura
        forca_consciente : float
            Intensidade da força consciente
        """
        self.posicao = np.array(posicao_inicial, dtype=float)
        self.velocidade = np.array(velocidade_inicial, dtype=float)
        self.horizonte_previsao = horizonte_previsao
        self.forca_consciente = forca_consciente
        self.trajetoria: List[Tuple[float, float]] = [tuple(self.posicao)]

    def densidade_entropica(self, posicao: np.ndarray) -> float:
        """
        Calcula a densidade entrópica em uma posição.
        Modelo: Entropia máxima no centro (buraco negro entrópico).

        Parameters:
        -----------
        posicao : np.ndarray
            Posição (x, y)

        Returns:
        --------
        float
            Densidade entrópica (maior = mais atraente)
        """
        distancia = np.linalg.norm(posicao)
        if distancia < 1.0:
            return 1000.0  # Centro muito atrativo
        return 1.0 / (distancia ** 2)  # Decai com 1/r²

    def prever_entropia_futura(self, posicao: np.ndarray, velocidade: np.ndarray,
                              passos: int) -> float:
        """
        Prevê a entropia futura baseada em movimento projetado.

        Parameters:
        -----------
        posicao : np.ndarray
            Posição atual
        velocidade : np.ndarray
            Velocidade atual
        passos : int
            Número de passos para prever

        Returns:
        --------
        float
            Entropia prevista
        """
        pos_futura = posicao + velocidade * passos
        return self.densidade_entropica(pos_futura)

    def decidir_movimento_consciente(self, temperatura: float = 0.1) -> np.ndarray:
        """
        Decide o próximo movimento baseado em previsão entrópica.
        A consciência busca reduzir entropia local (escapar do centro).

        Parameters:
        -----------
        temperatura : float
            Agitação térmica para decisões probabilísticas

        Returns:
        --------
        np.ndarray
            Vetor de aceleração consciente
        """
        # Prever entropia atual e futura
        entropia_atual = self.densidade_entropica(self.posicao)
        entropia_futura = self.prever_entropia_futura(
            self.posicao, self.velocidade, self.horizonte_previsao
        )

        # Vetor radial (direção do centro)
        vetor_radial = -self.posicao / np.linalg.norm(self.posicao)

        # Se entropia futura > atual, tendência a cair (gravidade)
        # Consciência aplica força oposta para escapar
        if entropia_futura > entropia_atual:
            # Aplicar força anti-gravidade (para fora)
            forca_anti_grav = vetor_radial * self.forca_consciente
        else:
            # Manter órbita: força tangencial
            velocidade_tangencial = np.array([-self.velocidade[1], self.velocidade[0]])
            velocidade_tangencial = velocidade_tangencial / np.linalg.norm(velocidade_tangencial)
            forca_anti_grav = velocidade_tangencial * self.forca_consciente * 0.5

        # Adicionar ruído térmico
        ruido = np.random.normal(0, temperatura, 2)
        forca_total = forca_anti_grav + ruido

        return forca_total

    def atualizar_fisica(self, dt: float = 0.1):
        """
        Atualiza posição e velocidade usando física newtoniana simples.

        Parameters:
        -----------
        dt : float
            Passo de tempo
        """
        # Calcular força consciente
        aceleracao = self.decidir_movimento_consciente()

        # Atualizar velocidade
        self.velocidade += aceleracao * dt

        # Atualizar posição
        self.posicao += self.velocidade * dt

        # Registrar trajetória
        self.trajetoria.append(tuple(self.posicao))

    def simular_orbita(self, steps: int = 1000, dt: float = 0.1) -> List[Tuple[float, float]]:
        """
        Simula a órbita do agente consciente.

        Parameters:
        -----------
        steps : int
            Número de passos da simulação
        dt : float
            Passo de tempo

        Returns:
        --------
        list
            Trajetória completa (x, y)
        """
        for _ in range(steps):
            self.atualizar_fisica(dt)

            # Parar se escapar muito longe
            if np.linalg.norm(self.posicao) > 100.0:
                break

        return self.trajetoria

def comparar_agente_vs_materia_inerte(posicao_inicial: Tuple[float, float] = (10.0, 0.0),
                                     velocidade_inicial: Tuple[float, float] = (0.0, 1.0),
                                     steps: int = 500):
    """
    Compara trajetória de agente consciente vs matéria inerte.

    Parameters:
    -----------
    posicao_inicial : tuple
        Posição inicial
    velocidade_inicial : tuple
        Velocidade inicial
    steps : int
        Passos da simulação

    Returns:
    --------
    tuple
        (trajetoria_consciente, trajetoria_inerte)
    """
    # Agente consciente
    agente = AgenteConsciente(posicao_inicial, velocidade_inicial)
    traj_consciente = agente.simular_orbita(steps)

    # Matéria inerte (queda entrópica simples em 2D)
    pos_inerte = np.array(posicao_inicial, dtype=float)
    vel_inerte = np.array(velocidade_inicial, dtype=float)
    traj_inerte = [tuple(pos_inerte)]

    for _ in range(steps):
        # Movimento aleatório + atração entrópica
        ruido = np.random.normal(0, 0.1, 2)
        vetor_radial = -pos_inerte / np.linalg.norm(pos_inerte)
        atracao = vetor_radial * 0.05  # Força gravitacional simples

        vel_inerte += atracao + ruido
        pos_inerte += vel_inerte * 0.1
        traj_inerte.append(tuple(pos_inerte))

        if np.linalg.norm(pos_inerte) < 1.0:
            break

    return traj_consciente, traj_inerte

def plotar_comparacao(traj_consciente: List[Tuple[float, float]],
                      traj_inerte: List[Tuple[float, float]],
                      salvar: bool = True):
    """
    Plota comparação entre agente consciente e matéria inerte.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Centro (buraco negro entrópico)
    centro = plt.Circle((0, 0), 1.0, color='black', alpha=0.3, label='Buraco Negro Entrópico')
    ax.add_patch(centro)

    # Trajetória consciente
    x_c, y_c = zip(*traj_consciente)
    ax.plot(x_c, y_c, 'b-', linewidth=2, label='Agente Consciente (Anti-Gravidade)', alpha=0.8)

    # Trajetória inerte
    x_i, y_i = zip(*traj_inerte)
    ax.plot(x_i, y_i, 'r-', linewidth=2, label='Matéria Inerte (Gravidade)', alpha=0.8)

    ax.set_xlabel('Posição X')
    ax.set_ylabel('Posição Y')
    ax.set_title('Consciência como Anti-Gravidade: Agente vs Matéria Inerte')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axis('equal')

    if salvar:
        plt.savefig('images/comparacao_consciente_inerte.png', dpi=300, bbox_inches='tight')
        print("Figura salva como 'images/comparacao_consciente_inerte.png'")

    plt.show()

if __name__ == "__main__":
    # Demonstração
    print("=== DEMONSTRAÇÃO: Agente Consciente vs Matéria Inerte ===")

    traj_consciente, traj_inerte = comparar_agente_vs_materia_inerte()

    print(f"Agente consciente: {len(traj_consciente)} pontos na trajetória")
    print(f"Matéria inerte: {len(traj_inerte)} pontos na trajetória")

    # Calcular distâncias finais
    pos_final_consciente = np.array(traj_consciente[-1])
    pos_final_inerte = np.array(traj_inerte[-1])

    dist_consciente = np.linalg.norm(pos_final_consciente)
    dist_inerte = np.linalg.norm(pos_final_inerte)

    print(".2f")
    print(".2f")

    if dist_consciente > dist_inerte:
        print("✅ Agente consciente escapou mais longe - Anti-gravidade demonstrada!")
    else:
        print("❌ Agente não escapou - ajustar parâmetros")

    plotar_comparacao(traj_consciente, traj_inerte)