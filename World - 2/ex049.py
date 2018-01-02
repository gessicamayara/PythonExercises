#Refaça o desafio 009, mostrando a tabuada de um número
#que o usuario escolher, so que agora utilizando um laço for.

num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
