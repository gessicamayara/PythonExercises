#Faça um programa que leia o sexo de uma
#pessoa, mas so aceite os valores 'm' e 'f'.
#Caso esteja errado, peça a digitação novamente
#ate um valor correto.


sexo = str(input('Qual o seu sexo ? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor escreva seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
