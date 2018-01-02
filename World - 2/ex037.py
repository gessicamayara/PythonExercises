#Escreva um programa que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: [1] binario, [2] octal, [3] hexadecimal

num = int(input('Digite um número para converter: '))
print('''Escolha uma das bases  para conversão: 
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL 
''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em BINARIO é {}'.format(num, bin(num)[2:])) #Pulando duas casas para mostrar apenas os números
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida! Tente novamente! ')
