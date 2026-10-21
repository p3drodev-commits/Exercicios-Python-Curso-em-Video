# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

computador = random.randint(0, 5)

usuario = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 5): '))

if usuario == computador:
    print(f'Parabéns! Você acertou! O número era {computador}.')

else:
    print(f'Que pena! Você errou. O número era {computador}.')