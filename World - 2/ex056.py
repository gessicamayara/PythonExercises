#Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas.
#No final do programa, mostre:
#A media de idade do grupo
#Quantas mulheres tem menos de 20 anos
#Qual é o nome do homem mais velho.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A media de idade é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('O total de mulheres com idade maior que 20 é {}'.format(totmulher))
