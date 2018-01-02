#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#A vista Dinheiro/Cheque:
#10% de desconto
#A vista no cartão:
#5% de desconto
#Em ate 2x no cartão:
#preço normal
#3x ou mais no cartão:
#20% de juros

preco = float(input('Digite o valor da compra: '))
opcao = int(input(''' Qual a forma de pagamento?
[1] A vista Dinheiro/Cheque
[2] A vista Cartão
[3] Em ate 2x no cartão
[4] 3x ou mais no cartão
'''))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
