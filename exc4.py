#  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print(f'É um valor identificador? {algo.isidentifier()};')
print(f'É uma palavra? {type(algo)};')
print(f'É um número inteiro? {algo.isnumeric()};')
print(f'É um valor boleano? {algo.isboolean()};')
print(f'É um valor alfanumérico? {algo.isalnum()};')
print(f'É um valor alfabético? {algo.isalpha()};')
print(f'É um valor decimal? {algo.isdecimal()};')
print(f'É um valor digito? {algo.isdigit()};')
