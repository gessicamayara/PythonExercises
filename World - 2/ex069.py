'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A: Quantas pessoas tem mais de 18 anos.
B: Quantos homens foram cadastrados.
C: Quantas mulheres tem menos de 20 anos.'''

tot18 = totman = totwoman = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totman += 1
    if sexo == 'F' and idade < 20:
        totwoman += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de  18 anos: {tot18}')
print(f'Ao todo temos {totman} homens cadastrados')
print(f'E temos {totwoman} mulheres com menos de 20 anos')
