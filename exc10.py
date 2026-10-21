# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# valor do dólar = R$ 5,18 (30/09/2026)

valor = float(input('Digite o valor em reais que você tem na carteira: R$ '))

print(f'Com R${valor:.2f}, você pode comprar US${valor/5.18:.2f}.')
