#  Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f'O preço da passagem para uma viagem de {distancia:.2f} km é de R${preco_passagem:.2f}.')

else:
    preco_passagem = distancia * 0.45
    print(f'O preço da passagem para uma viagem de {distancia:.2f} km é de R${preco_passagem:.2f}.')
