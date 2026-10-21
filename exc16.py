# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import random

num = random.uniform(1, 100)

print(f'O número sorteado foi {num:.2f} e sua porção inteira é {int(num)}')