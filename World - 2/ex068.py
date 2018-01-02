#Faça um programa que jogue par ou impar com o computador.
# O jogo so sera interrompido quando o jogador perder, monstrando o
# total de vitorias consecutivas que ele conquistou no final

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
             if total % 2 == 1:
                print('Voce venceu!')
                v += 1
             else:
                print('Voce perdeu!')
                break
    print('Vamos jogar novamente? ')
print(f'GAME OVER! Voce venceu {v} vezes ')
