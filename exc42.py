#  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

reta_1 = int(input('Digite o comprimento da primeira reta: '))
reta_2 = int(input('Digite o comprimento da segunda reta: '))
reta_3 = int(input('Digite o comprimento da terceira reta: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('As retas podem formar um triângulo.')
    if reta_1 == reta_2 == reta_3:
        print('O triângulo é EQUILÁTERO.')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('O triângulo é ISÓSCELES.')
    else:
        print('O triângulo é ESCALENO.')
else:
    print('As retas não podem formar um triângulo.')