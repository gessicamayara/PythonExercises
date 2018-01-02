#Faça um programa que leia três números e mostre qual deles é o maior e qual é o menor

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = b
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
