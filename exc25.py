# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome da pessoa: '))

if 'SILVA' in nome.upper():
    print('O nome da pessoa contém SILVA.')

else: 
    print('O nome da pessoa não contém SILVA.')