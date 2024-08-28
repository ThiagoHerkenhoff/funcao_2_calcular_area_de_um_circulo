"""
Exercício: Calcular a Área de um Círculo

Escreva uma função chamada calcular_area_circulo que receba como parâmetro o raio de um
círculo e retorne a área do círculo. A fórmula para calcular a área de um
círculo é: Area=π×raio2

Onde:

    π (pi) é aproximadamente 3.14159
    O raio é a distância do centro do círculo até a borda.

Dicas:

    Use a constante math.pi do módulo math para o valor de π.
    Lembre-se de importar o módulo math no início do seu script.

"""

import math
""" Import da biblioteca math """


def calcular_area_circulo(raio):
    """ Função criada conforme solicitado no exercicio """
    return math.pi * (raio ** 2)
""" saida de dado com o calculo da area de um circulo: area = π * raio² """

print(calcular_area_circulo(5))
""" Execução e impressão na tela do resultado """