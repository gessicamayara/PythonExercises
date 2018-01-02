#Faça um programa que calcule a soma entrem todos os numeros
#impares que sao multiplos de tres e que se encontram no invervalo de 1 ate 500

soma = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            cont = cont + 1
            soma = soma + c
print('O valor de todos os {} valores é {}'.format(cont, soma))

