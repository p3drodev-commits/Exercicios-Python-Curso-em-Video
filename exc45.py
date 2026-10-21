# GAME PEDRA, PAPEL, TESOURA

import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Suas opções:)
[0] = 'Pedra'
[1] = 'Papel'
[2] = 'Tesoura' ''')

jogador = int(input('Qual é a sua jogada?  '))

print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')



elif computador == 2:    
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('COMPUTADOR VENCE!')

    elif jogador == 2: 
        print('EMPATE!')       

    else:
        print('JOGADA INVÁLIDA!')
