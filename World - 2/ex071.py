'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergutando ao usuario qual
o valor a ser sacado(inteiros), e o programa irá informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa tenha cédulas de R$50, $20, R$10 e R$1.'''

print('='*30)
print('{:-^30}'.format('BANCO PYTHON'))
print('='*30)
valor = int(input('Qual o valor você quer sacar R$ ? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= 50:
        total -=50
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
            if ced ==50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if total ==0:
                break
