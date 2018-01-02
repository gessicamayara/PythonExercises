#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e moestre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 ate 30: Sobrepeso
#30 ate 40: Obesidade
#Acima de 40: Obesidade morbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc <= 25 and imc < 30:
    print('Obesidade')
else:
    print('Obesidade morbida')
