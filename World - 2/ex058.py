#Melhore o jogo do desafio 028 onde o computador vai
#'pensar' em um número de 0 a 10. Só que agora o jogador
#vai tentar adivinhar até acertar, mostrando no final
#quantos palpites foram necessários para vencer.

from random import randint
print('Vou pensar em um número... Tente adivinhar!')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} palpites'.format(palpites))
