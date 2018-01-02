#Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro
#e o ultimo nome, separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
