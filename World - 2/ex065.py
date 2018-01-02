#Crie um programa que leia vários números inteiros pelo teclado
#e no final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valores lidos. O programa deve perguntar
#ao usuario se ele quer ou não continuar a digitar valores.

resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite  um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = maior
        if num < menor:
            menor = num
    resp = str(input('Quer continuar : [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
