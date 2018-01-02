#Faça um programa que leia um número qualquer, e mostre se ele é bissexto
#(Um ano bissexto é o ano que tem um dia a mais)
from datetime import date
ano = int(input('Que ano voce quer analizar? Coloque 0 para atualizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O  ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
