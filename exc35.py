# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = int(input('Digite o comprimento da primeira reta: '))
reta_2 = int(input('Digite o comprimento da segunda reta: '))
reta_3 = int(input('Digite o comprimento da terceira reta: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')