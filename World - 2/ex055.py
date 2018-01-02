#Faça um programa que leia o peso de cinco pessoas. No final,
#mostre qual foi o maior e o menor peso lidos.

print('\033[1;33m{}\033[m'.format('=+' * 40))
print('{:^80}'.format('Olá,Seja bem vindo'))
print('\033[1;33m{}\033[m'.format('=+' * 40))
print('')

peso = float(input('Digite algum peso: ').strip())
maior = 0
menor = peso
for contador in range(0, 5):
    peso = float(input('Digite algum peso: ').strip())
    if peso <= menor:
        menor = peso
    if peso > maior:
        maior = peso

print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
