#Crie um programa que leia o ano de nascimento de sete pessoas. No
#final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}ª nasceu?'.format(pessoa)))
    idade = atual - nascimento
    if idade>= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivenos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))
