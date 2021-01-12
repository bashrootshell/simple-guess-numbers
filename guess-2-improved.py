#!/usr/bin/env python3

from random import randrange
# from numpy.random import randint

"""
    Jogo de adivinhação com números de 1 a 30.
    Máximo de 9 tentativas.
    Executa validação de entrada.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

numero = randrange(1, 30)
# numero = randint(1, 30, 1)

try:

    for tentativa in range(1, 9):

        print(f'Tentativa {tentativa} de 8. Digite um número entre 1 e 30.')
        chute = int(input())

        if chute > 30 or chute < 1:
            print('Digite um número entre 1 e 30!')
            break
        elif chute < numero:
            if tentativa == 8:
                print(f'Não foi desta vez. O número escolhido foi o {numero}.')
                break
            print('Seu chute foi muito baixo!')
        elif chute > numero:
            if tentativa == 8:
                print(f'Não foi desta vez. O número escolhido foi o {numero}.')
                break
            print('Seu chute foi muito alto!')
        else:
            print(f'Ótimo! Acertou o número {numero} em {tentativa} chutes!')
            break

except KeyboardInterrupt:
    print('Interrupção via Ctrl-C')

except ValueError as erro:
    print(f'>>> Erro "{erro}" <<< \n Digite apenas dígitos entre 1 e 30.')
