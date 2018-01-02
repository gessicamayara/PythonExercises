#Melhore o desafio 061, perguntando ao usuario se ele quer mostrar
#mais alguns termos. O programa encerra quando ele disser que
#quer mostrar 0 termos.

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont += 1

    print('PAUSA')
    mais = int(input('Quantos termos voce quer ler a mais?'))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))
