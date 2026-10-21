# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
angulo_rad = radians(angulo)

print(f'O ângulo de {angulo} tem o SENO de {sin(angulo_rad):.2f}')
print(f'O seu COSSENO é {cos(angulo_rad):.2f}')
print(f'E a sua TANGENTE é {tan(angulo_rad):.2f}')