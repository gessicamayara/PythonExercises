#Escreva um programa e que leia o comprimento de 3 retas e informe se é possível
#formar um triangulo.

r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
