# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#- Acima de 40: Obesidade Mórbida

# PARA ESTE PROGRAMA EU CHAMEI ALTURA DE 'h' e PESO DE 'p'

h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))

imc = p / (h ** 2)

print(f'Seu IMC é de {imc:.2f}.')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')