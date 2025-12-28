"""
Módulo Galáxia Consciente: Livre Arbítrio contra Determinismo Cósmico

Este módulo integra o Agente Consciente com a simulação galáctica entrópica,
demonstrando que seres conscientes podem navegar contra o fluxo determinista
do universo, provando livre arbítrio absoluto.

Objetivo: Mostrar que a consciência permite escapar do determinismo cósmico.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional, Dict
from src.agente_consciente import AgenteConsciente
from src.rotacao_galactica import forca_verlinde, velocidade_orbital_estavel

class GalaxiaConsciente:
    """
    Simulação de galáxia com agentes conscientes navegando contra fluxo entrópico.

    Demonstra que seres conscientes podem exercer livre arbítrio contra
    o determinismo gravitacional do universo.
    """

    def __init__(self, raio_galaxia: float = 100.0,
                 num_estrelas: int = 50,
                 centro_massa: float = 1000.0):
        """
        Inicializa galáxia consciente.

        Parameters:
        -----------
        raio_galaxia : float
            Raio da galáxia em unidades
        num_estrelas : int
            Número de estrelas orbitando
        centro_massa : float
            Massa no centro galáctico
        """
        self.raio_galaxia = raio_galaxia
        self.num_estrelas = num_estrelas
        self.centro_massa = centro_massa

        # Criar estrelas em órbitas estáveis (matéria inerte)
        self.estrelas = self._criar_estrelas_inertes()

        # Agente consciente (único por enquanto)
        self.agente_consciente = None

    def _criar_estrelas_inertes(self) -> List[Dict]:
        """
        Cria estrelas que seguem leis físicas deterministas (matéria inerte).

        Returns:
        --------
        list
            Lista de dicionários com estado de cada estrela
        """
        estrelas = []

        # Raios distribuídos logaritmicamente
        raios = np.logspace(np.log10(5), np.log10(self.raio_galaxia), self.num_estrelas)

        for i, r in enumerate(raios):
            # Ângulo inicial aleatório
            angulo = np.random.uniform(0, 2*np.pi)

            # Posição inicial
            x = r * np.cos(angulo)
            y = r * np.sin(angulo)

            # Velocidade orbital estável (Verlinde)
            v_orbital = velocidade_orbital_estavel(r, 'verlinde')

            # Velocidade tangencial
            vx = -v_orbital * np.sin(angulo)  # perpendicular à posição
            vy = v_orbital * np.cos(angulo)

            estrela = {
                'id': i,
                'posicao': np.array([x, y]),
                'velocidade': np.array([vx, vy]),
                'raio_orbital': r,
                'trajetoria': [np.array([x, y])],
                'tipo': 'inerte'
            }
            estrelas.append(estrela)

        return estrelas

    def adicionar_agente_consciente(self,
                                   posicao_inicial: Tuple[float, float] = (20.0, 0.0),
                                   velocidade_inicial: Tuple[float, float] = (0.0, 2.0),
                                   objetivo: Optional[Tuple[float, float]] = None):
        """
        Adiciona agente consciente à galáxia.

        Parameters:
        -----------
        posicao_inicial : tuple
            Posição inicial do agente
        velocidade_inicial : tuple
            Velocidade inicial
        objetivo : tuple, optional
            Objetivo do agente (estrela específica ou saída da galáxia)
        """
        self.agente_consciente = AgenteConsciente(
            posicao_inicial=posicao_inicial,
            velocidade_inicial=velocidade_inicial,
            horizonte_previsao=10,  # Maior previsão para navegação consciente
            forca_consciente=0.5    # Força consciente aumentada
        )

        self.objetivo_agente = objetivo

        # Se não especificado, objetivo é sair da galáxia (raio > raio_galaxia)
        if objetivo is None:
            # Objetivo: escapar para 1.5x o raio galáctico
            direcao = np.array(posicao_inicial) / np.linalg.norm(posicao_inicial)
            self.objetivo_agente = tuple(direcao * self.raio_galaxia * 1.5)

    def _calcular_aceleracao_consciente(self, agente: AgenteConsciente) -> np.ndarray:
        """
        Calcula aceleração consciente considerando objetivo do agente.

        Parameters:
        -----------
        agente : AgenteConsciente
            O agente consciente

        Returns:
        --------
        np.ndarray
            Vetor aceleração consciente
        """
        if self.objetivo_agente is None:
            # Sem objetivo específico: apenas escapar da atração entrópica
            return agente.decidir_movimento_consciente()

        # Objetivo específico: navegar em direção ao objetivo
        pos_objetivo = np.array(self.objetivo_agente)
        vetor_objetivo = pos_objetivo - agente.posicao
        distancia_objetivo = np.linalg.norm(vetor_objetivo)

        if distancia_objetivo < 5.0:  # Chegou ao objetivo
            return np.zeros(2)  # Parar

        # Direção para o objetivo
        direcao_objetivo = vetor_objetivo / distancia_objetivo

        # Força gravitacional entrópica (que tenta manter em órbita)
        r = np.linalg.norm(agente.posicao)
        aceleracao_gravitacional = forca_verlinde(r)
        vetor_radial = -agente.posicao / r
        forca_grav = aceleracao_gravitacional * vetor_radial

        # Força consciente: contrabalançar gravidade + ir para objetivo
        forca_contra_grav = -forca_grav * agente.forca_consciente
        forca_para_objetivo = direcao_objetivo * agente.forca_consciente * 0.5

        # Combinação: escapar da órbita + ir para objetivo
        aceleracao_total = forca_contra_grav + forca_para_objetivo

        # Adicionar ruído para simular tomada de decisão
        ruido = np.random.normal(0, 0.1, 2)
        return aceleracao_total + ruido

    def atualizar_fisica_estrelas(self, dt: float = 0.1):
        """
        Atualiza física das estrelas inertes (deterministas).
        """
        for estrela in self.estrelas:
            pos = estrela['posicao']
            vel = estrela['velocidade']

            r = np.linalg.norm(pos)

            # Aceleração gravitacional (Verlinde)
            aceleracao = forca_verlinde(r)
            vetor_radial = -pos / r
            acel = aceleracao * vetor_radial

            # Atualizar velocidade e posição
            vel += acel * dt
            pos += vel * dt

            # Registrar trajetória
            estrela['trajetoria'].append(pos.copy())

    def atualizar_agente_consciente(self, dt: float = 0.1):
        """
        Atualiza agente consciente com livre arbítrio.
        """
        if self.agente_consciente is None:
            return

        # Calcular aceleração consciente (livre arbítrio)
        aceleracao_consciente = self._calcular_aceleracao_consciente(self.agente_consciente)

        # Aplicar aceleração
        self.agente_consciente.velocidade += aceleracao_consciente * dt
        self.agente_consciente.posicao += self.agente_consciente.velocidade * dt

        # Registrar trajetória
        self.agente_consciente.trajetoria.append(tuple(self.agente_consciente.posicao))

    def simular_galaxia(self, passos: int = 1000, dt: float = 0.1) -> Dict:
        """
        Simula evolução da galáxia com agente consciente.

        Parameters:
        -----------
        passos : int
            Número de passos da simulação
        dt : float
            Passo de tempo

        Returns:
        --------
        dict
            Resultados da simulação
        """
        print(f"Simulando galáxia com {self.num_estrelas} estrelas inertes...")

        for passo in range(passos):
            # Atualizar estrelas deterministas
            self.atualizar_fisica_estrelas(dt)

            # Atualizar agente consciente (livre arbítrio)
            self.atualizar_agente_consciente(dt)

            # Verificar se agente conseguiu escapar
            if self.agente_consciente:
                r_agente = np.linalg.norm(self.agente_consciente.posicao)
                if r_agente > self.raio_galaxia * 1.2:  # Escapou
                    print(f"✅ Agente consciente ESCAPOU da galáxia no passo {passo}!")
                    break

                # Verificar se chegou ao objetivo
                if self.objetivo_agente:
                    dist_objetivo = np.linalg.norm(
                        np.array(self.objetivo_agente) - self.agente_consciente.posicao
                    )
                    if dist_objetivo < 5.0:
                        print(f"🎯 Agente consciente CHEGOU ao objetivo no passo {passo}!")
                        break

        return self._analisar_resultados()

    def _analisar_resultados(self) -> Dict:
        """
        Analisa resultados da simulação.

        Returns:
        --------
        dict
            Análise completa dos resultados
        """
        resultados = {
            'estrelas_inertes': len(self.estrelas),
            'trajetorias_inertes': [estrela['trajetoria'] for estrela in self.estrelas],
            'agente_consciente': None,
            'sucesso_escape': False,
            'sucesso_objetivo': False,
            'livre_arbitrio_demonstrado': False
        }

        if self.agente_consciente:
            resultados['agente_consciente'] = {
                'trajetoria': self.agente_consciente.trajetoria,
                'posicao_final': tuple(self.agente_consciente.posicao),
                'distancia_final': np.linalg.norm(self.agente_consciente.posicao)
            }

            # Verificar sucesso
            r_final = np.linalg.norm(self.agente_consciente.posicao)
            resultados['sucesso_escape'] = r_final > self.raio_galaxia * 1.2

            if self.objetivo_agente:
                dist_obj = np.linalg.norm(
                    np.array(self.objetivo_agente) - self.agente_consciente.posicao
                )
                resultados['sucesso_objetivo'] = dist_obj < 5.0

            # Livre arbítrio demonstrado se conseguiu escapar OU chegar ao objetivo
            resultados['livre_arbitrio_demonstrado'] = (
                resultados['sucesso_escape'] or resultados['sucesso_objetivo']
            )

        return resultados

    def plotar_galaxia_consciente(self, salvar: bool = True) -> None:
        """
        Plota galáxia com agente consciente navegando.

        Parameters:
        -----------
        salvar : bool
            Se deve salvar a figura
        """
        fig, ax = plt.subplots(figsize=(12, 12))

        # Centro galáctico
        centro = plt.Circle((0, 0), 2.0, color='black', alpha=0.8, label='Buraco Negro Central')
        ax.add_patch(centro)

        # Estrelas inertes (trajetórias)
        for estrela in self.estrelas:
            traj = estrela['trajetoria']
            if len(traj) > 1:
                x_traj, y_traj = zip(*traj)
                ax.plot(x_traj, y_traj, 'b-', alpha=0.3, linewidth=1)

        # Posições finais das estrelas
        for estrela in self.estrelas:
            pos_final = estrela['trajetoria'][-1]
            ax.scatter(pos_final[0], pos_final[1], color='blue', s=20, alpha=0.6)

        # Agente consciente
        if self.agente_consciente:
            traj_agente = self.agente_consciente.trajetoria
            if len(traj_agente) > 1:
                x_agent, y_agent = zip(*traj_agente)
                ax.plot(x_agent, y_agent, 'r-', linewidth=3, label='Agente Consciente', alpha=0.8)

                # Posição inicial
                pos_inicial = traj_agente[0]
                ax.scatter(pos_inicial[0], pos_inicial[1], color='red', s=100,
                          marker='*', label='Início Agente')

                # Posição final
                pos_final = traj_agente[-1]
                ax.scatter(pos_final[0], pos_final[1], color='red', s=150,
                          marker='X', label='Fim Agente')

        # Objetivo do agente
        if self.objetivo_agente:
            ax.scatter(self.objetivo_agente[0], self.objetivo_agente[1],
                      color='green', s=150, marker='^', label='Objetivo')

        # Configurações do plot
        ax.set_xlabel('Posição X')
        ax.set_ylabel('Posição Y')
        ax.set_title('Galáxia Consciente: Livre Arbítrio contra Determinismo Cósmico\n'
                    '(Agente vermelho navegando contra fluxo entrópico azul)')
        ax.legend()
        ax.axis('equal')
        ax.grid(True, alpha=0.3)

        # Círculo da galáxia
        galaxia_circle = plt.Circle((0, 0), self.raio_galaxia,
                                   color='gray', fill=False, linestyle='--', alpha=0.5)
        ax.add_patch(galaxia_circle)

        if salvar:
            plt.savefig('images/galaxia_consciente_livre_arbitrio.png', dpi=300, bbox_inches='tight')
            print("💾 Figura salva: 'images/galaxia_consciente_livre_arbitrio.png'")

        plt.show()

def demonstracao_livre_arbitrio():
    """
    Demonstração completa: Agente consciente navegando contra determinismo galáctico.
    """
    print("=" * 80)
    print("DEMONSTRAÇÃO: LIVRE ARBÍTRIO CONTRA DETERMINISMO CÓSMICO")
    print("=" * 80)
    print()
    print("Objetivo: Provar que seres conscientes podem escolher seu destino")
    print("contra o fluxo determinista do universo.")
    print()

    # Criar galáxia
    galaxia = GalaxiaConsciente(raio_galaxia=80.0, num_estrelas=30)

    # Adicionar agente consciente com objetivo de escapar
    galaxia.adicionar_agente_consciente(
        posicao_inicial=(25.0, 0.0),    # Dentro da galáxia
        velocidade_inicial=(0.0, 3.0),  # Velocidade orbital inicial
        objetivo=None  # Objetivo: escapar da galáxia
    )

    print("Configuração:")
    print(f"- Galáxia: {galaxia.num_estrelas} estrelas inertes")
    print(f"- Agente consciente: Posição inicial (25, 0), objetivo = ESCAPAR")
    print()

    # Simular
    resultados = galaxia.simular_galaxia(passos=1500)

    print()
    print("RESULTADOS DA SIMULAÇÃO:")
    print("-" * 40)

    if resultados['agente_consciente']:
        agent_data = resultados['agente_consciente']
        print(".1f")
        print(".1f")

        if resultados['sucesso_escape']:
            print("✅ LIVRE ARBÍTRIO DEMONSTRADO!")
            print("   O agente consciente ESCAPOU do determinismo galáctico.")
            print("   Prova: Consciência permite escolher contra fluxo cósmico.")
        elif resultados['sucesso_objetivo']:
            print("🎯 OBJETIVO ALCANÇADO!")
            print("   Agente navegou para destino específico contra gravidade.")
        else:
            print("⚠️  NAVEGAÇÃO PARCIAL")
            print("   Agente mostrou resistência mas não escapou completamente.")
            print("   Ajustar parâmetros de força consciente.")

    print()
    print("INTERPRETAÇÃO FILOSÓFICA:")
    print("- Galáxia (Azul) = Determinismo do universo/sociedade")
    print("- Agente (Vermelho) = Você/Consciência individual")
    print("- Escape = Livre arbítrio contra corrente cósmica")

    # Plotar
    galaxia.plotar_galaxia_consciente(salvar=True)

    return resultados

if __name__ == "__main__":
    demonstracao_livre_arbitrio()