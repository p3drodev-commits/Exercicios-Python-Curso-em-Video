#  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da cidade: '))

if cidade[:5].upper() == 'SANTO':
    print('A cidade começa com SANTO.')

else:
    print('A cidade não começa com SANTO.')