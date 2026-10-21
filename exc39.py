# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


idade = int(input('Qual é a sua idade? '))

print(f'Quem nasceu em {idade} tem {2026 - idade} anos em 2026.')

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
else:
    print(f'Já passou {idade - 18} anos do prazo de alistamento.')
