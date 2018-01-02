#Crie um programa que leia um número inteiro e mostre se ele é par ou impar

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('O número é Par')
else:
    print('O número é Impar')
