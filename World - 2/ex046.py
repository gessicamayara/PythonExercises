#Faça um programa que mostre na tela uma contagem regressiva para o
#estouro dos fogos de artificio, indo de 10 ate 0, com uma pausa de
#1 segundo entre eles.

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)

print('BUM! BUM! BUM!')
