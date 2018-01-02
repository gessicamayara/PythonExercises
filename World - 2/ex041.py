#A confederação Nacional de Natação precisa de um programa que leia o ano
#de nascimento de um atleta e mostre sua categoria de acordo com a idade:
#Ate 9 anos: MIRIM
#Ate 14 anos: INFANTIL
#Ate 19 anos: JUNIOR
#Ate 25 anos: SENIOR
#Acima: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Digite  o ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    idade > 25
    print('Categoria Master')
