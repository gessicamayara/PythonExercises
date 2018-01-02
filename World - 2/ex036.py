#Escreva um programa para aprovar  o emprestimo bancario para compra de uma casa
#Perguntar o valor da casa, o salario, e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salario, se nao o emprestimo será negado.


casa = float(input('Qual  o valor da casa?  '))
salario = float(input('Qual o valor do salario? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/ (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será R${:.2f}'.format(prestacao))
if salario <= minimo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo negado!')
