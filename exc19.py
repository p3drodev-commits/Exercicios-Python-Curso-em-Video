# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alunos= ['João', 'Maria', 'José', 'Ana']

sorteado = random.choice(alunos)

print(f'Os alunos são: {', '.join(alunos)}')
print(f'O aluno sorteado foi: {sorteado}')