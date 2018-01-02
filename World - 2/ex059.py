#Crie um programa que leia dois valores e mostre um menu com as opçoes:
#[1]somar [2]multiplicar [3]maior [4] novos numeros []5 sair do programa

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite  o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Insira os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao ==5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente.')
        sleep(2)
print('Fim do programa')
