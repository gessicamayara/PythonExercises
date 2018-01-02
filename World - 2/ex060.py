#Faça um programa que leia um número e mostre o seu fatorial

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else ' = ', end='  ')
    f *=c
    c -=1
print('{}'.format(f))
