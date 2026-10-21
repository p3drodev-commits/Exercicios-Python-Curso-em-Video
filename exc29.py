# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.


velocidade_carro = float(input('Digite a velocidade do carro em km/h: '))

if velocidade_carro > 80:
    print('Você foi multado! A multa é de R$7,00 por cada km acima do limite.')
    km_acima = velocidade_carro - 80
    multa = km_acima * 7
    print(f'Você excedeu {km_acima:.2f} km/h acima do limite. O valor da multa é de R${multa:.2f}.')

else:
    print('Você está dentro do limite de velocidade. Dirija com segurança!')