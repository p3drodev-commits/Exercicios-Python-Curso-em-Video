#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: R$'))

print('Escolha a forma de pagamento:\n' \
'1 - À vista dinheiro/cheque\n'
'2 - À vista no cartão\n' \
'3 - Em até 2x no cartão\n' \
'4 - 3x ou mais no cartão')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    valor_final = valor - (valor * 0.10)
    print(f'O valor final do produto será de R${valor_final:.2f}.')
elif opcao == 2:
    valor_final = valor - (valor * 0.05)
    print(f'O valor final do produto será de R${valor_final:.2f}.')
elif opcao == 3:
    valor_final = valor
    print(f'O valor final do produto será de R${valor_final:.2f}.')
elif opcao == 4:
    valor_final = valor + (valor * 0.20)
    print(f'O valor final do produto será de R${valor_final:.2f}.')
else:
    print('Opção inválida!')