# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


cateto_oposto = float(input('Digite o comprimeto do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimeto do cateto adjacente: '))

from math import hypot, sqrt

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')

