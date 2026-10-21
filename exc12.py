#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: R$'))
novo_preco = preco - (preco * 0.05)

print(f'O novo preço do produto com 5% de desconto é: R${novo_preco:.2f}.')