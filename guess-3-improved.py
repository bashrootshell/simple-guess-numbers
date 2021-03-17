#!/usr/bin/env python3

from random import randint

""" v3 - código mais limpo
    Jogo de adivinhação com números de 1 a 30.
    Máximo de 8 tentativas.
    Executa validação de entrada.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

numero_aleatorio = randint(1, 30)  # número escolhido aleatoriamente
maximo_de_8_tentativas = range(1, 9)  # pool de tentativas, máximo de 8
entre_1_e_30 = range(1, 31)  # pool de números possíveis escolha do usuário

try:
    
    for tentativa in maximo_de_8_tentativas:  
        
        print(f'Tentativa {tentativa} de 8. Digite um número entre 1 e 30.')     
        chute_do_usuario = int(input("Número > "))
        
        #  se o número não for menor ou maior, será igual ao número aleatório
        if chute_do_usuario not in entre_1_e_30:
            exit('Digite um número entre 1 e 30!')
        elif chute_do_usuario < numero_aleatorio:
            print('O chute foi mais baixo do que o número aleatório!')       
        elif chute_do_usuario > numero_aleatorio:
            print('O chute foi mais alto do que o número aleatório!')        
        else:
            exit(f'Acertou! Número: {numero_aleatorio}')
    #  as 8 chances se esgotam aqui, fora do loop
    print(f'O número escolhido era: {numero_aleatorio}')

except (ValueError, KeyboardInterrupt) as erro:
    print(f'>>> Erro |{erro}| <<< \n')
