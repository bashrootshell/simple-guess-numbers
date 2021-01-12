#!/usr/bin/env python3

import random

"""
    Jogo de adivinhação com números de 1 a 16.
    Executa até encontrar o número certo.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

numero = random.randrange(1, 16)

print('Chute um número entre 1 and 16.')

while True:
    print('Tente um número...')
    chute = int(input())
    if chute < numero:
        print('Seu chute foi muito baixo.')
    elif chute > numero:
        print('Seu chute foi muito alto.')
    else:
        print(f'Ótimo! Acertou o número {numero}')
        break
