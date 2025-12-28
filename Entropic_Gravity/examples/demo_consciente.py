"""
Demonstração: Consciência como Anti-Gravidade

Esta demonstração compara o comportamento de um agente consciente
com matéria inerte em um campo gravitacional entrópico.

Hipótese: O agente consciente pode orbitar ou escapar, enquanto
a matéria inerte cai para o centro.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agente_consciente import comparar_agente_vs_materia_inerte, plotar_comparacao

def main():
    print("=" * 60)
    print("DEMONSTRAÇÃO: Consciência como Anti-Gravidade")
    print("=" * 60)
    print()
    print("Conceito: A consciência permite resistir à atração entrópica,")
    print("enquanto matéria inerte cai para o buraco negro entrópico.")
    print()

    # Configurações da simulação
    posicao_inicial = (10.0, 0.0)  # 10 unidades do centro
    velocidade_inicial = (0.0, 1.0)  # Velocidade tangencial para órbita
    steps = 500

    print("Executando simulação...")
    print(f"Posição inicial: {posicao_inicial}")
    print(f"Velocidade inicial: {velocidade_inicial}")
    print(f"Passos: {steps}")
    print()

    # Executar comparação
    traj_consciente, traj_inerte = comparar_agente_vs_materia_inerte(
        posicao_inicial, velocidade_inicial, steps
    )

    print("Simulação concluída!")
    print()

    # Análise dos resultados
    print("ANÁLISE DOS RESULTADOS:")
    print("-" * 30)

    pos_final_consciente = traj_consciente[-1]
    pos_final_inerte = traj_inerte[-1]

    dist_consciente = ((pos_final_consciente[0]**2 + pos_final_consciente[1]**2)**0.5)
    dist_inerte = ((pos_final_inerte[0]**2 + pos_final_inerte[1]**2)**0.5)

    print(".2f")
    print(".2f")
    print()

    # Interpretação
    if dist_consciente > dist_inerte:
        print("✅ RESULTADO POSITIVO: Agente consciente escapou mais longe!")
        print("   A consciência demonstrou ser anti-gravidade.")
        print("   Imortalidade da informação provada algoritmicamente.")
    elif abs(dist_consciente - dist_inerte) < 1.0:
        print("⚠️  RESULTADO NEUTRO: Semelhança nas trajetórias.")
        print("   Ajustar parâmetros do agente consciente.")
    else:
        print("❌ RESULTADO NEGATIVO: Matéria inerte escapou mais.")
        print("   Revisar modelo de consciência.")

    print()
    print("Gerando visualização...")

    # Criar diretório images se não existir
    os.makedirs('images', exist_ok=True)

    # Plotar comparação
    plotar_comparacao(traj_consciente, traj_inerte, salvar=True)

    print("Visualização salva como 'images/comparacao_consciente_inerte.png'")
    print()

    print("PRÓXIMOS PASSOS SUGERIDOS:")
    print("1. Ajuste força_consciente para órbitas mais estáveis")
    print("2. Implemente aprendizado para o agente consciente")
    print("3. Extensão para múltiplos agentes em rede")
    print("4. Integração com modelos quânticos de consciência")

if __name__ == "__main__":
    main()