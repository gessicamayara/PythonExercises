#Crie um programa que pergunte a distancia de uma viagem em km, calcule
#o preço da passagem, cobrando  R$0,50 por km, para viagens de  até 200 km é
#R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distancia da viagem em KM? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da viagem é R${:.2f}'.format(preco))
