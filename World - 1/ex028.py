#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5, e peça ao usuario tentar descobrir qual foi o número escolhido
#pelo computador. O programa deverá escrever na tela se o usuário venceu  a partida.

from random import randint
computador = randint(0, 5)
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*18)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Haha, Você perdeu! eu pensei no número {}'.format(computador))

