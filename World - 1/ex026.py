#Faça um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez
#Em qual posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "a" apareceu pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A ultima letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))
