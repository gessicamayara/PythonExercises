#Escreva um programa que leia o ano de nascimento de um jovem, e informe de acordo
#com a sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se
#alistar ou se já passou do tempo do alistamento. Seu programa deverá tambem mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para alistamento'.format(saldo))
else:
    idade > 18
    saldo = 18 + idade
    print('Voce ja deveria ter se alistado a {} anos'.format(saldo))
