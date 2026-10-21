#  Faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
tinta_necessaria = area / 2

print(f'A área da parede é de {area:.2f} metros quadrados.')
print(f'Você vai precisar de {tinta_necessaria:.2f} litros de tinta para pinta-la.')