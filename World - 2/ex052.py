#Faça um programa que leia um numero inteiro e diga se ele é
#ou nao um numero primo.

num = int(input('Digite um numero para verificar se ele é primo ou não: '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0 número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')

