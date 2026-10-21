# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['João', 'Maria', 'José', 'Ana']
random.shuffle(alunos)

print(f'A ordem de apresentação é: {", ".join(alunos)}')