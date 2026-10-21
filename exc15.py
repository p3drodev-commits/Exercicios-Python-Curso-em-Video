# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Qual a quantidade de km percorridos pelo carro? '))
dias_alugados = int(input('Quantos dias de aluguel? '))

preco_total = (dias_alugados * 60) + (km_percorridos * 0.15)

print(f'O preço total a pagar pelo aluguel do carro é: R${preco_total:.2f}.')