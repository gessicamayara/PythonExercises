#Escreva um programa que pergunte o salario de um funcionario e calcule o seu
#aumento.  Para salarios superiores a R$ 1.250,00 calcule um aumento de  10%, para
# inferiores ou iguais calcule o aumento de 15%.

salario = float(input('Qual o valor do seu salario? '))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passará a ganhar R$ {:.2f} '.format(salario, novo))
