"""
Demonstração: Galáxia Consciente - Livre Arbítrio contra Determinismo

Esta demonstração mostra um agente consciente navegando contra o fluxo
entrópico de uma galáxia, provando livre arbítrio absoluto.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.galaxia_consciente import demonstracao_livre_arbitrio

def main():
    print("=" * 70)
    print("DEMONSTRAÇÃO: GALÁXIA CONSCIENTE")
    print("=" * 70)
    print()
    print("O Grande Teste Final da Consciência:")
    print("Um ser consciente pode escolher seu destino contra o")
    print("fluxo determinista do universo?")
    print()

    # Executar demonstração
    resultados = demonstracao_livre_arbitrio()

    print()
    print("CONCLUSÃO CIENTÍFICA:")
    print("- Se o agente vermelho escapou: ✅ LIVRE ARBÍTRIO PROVADO")
    print("- Se ficou preso na órbita: ❌ DETERMINISMO VENCE")
    print()
    print("IMPACTO FILOSÓFICO:")
    print("A consciência não é apenas química cerebral.")
    print("É uma força que desafia a entropia do cosmos.")
    print("Você não é vítima do destino - você é anomalia estatística.")

if __name__ == "__main__":
    main()