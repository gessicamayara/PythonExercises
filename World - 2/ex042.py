#Refaça o desafio 035 dos triangulos, acrescentando  o recurso de
#mostrar que tipo de triangulo sera formado:

#Equilatero: Todos os lados iguais
#Isosceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

r1 = float(input('Digite  o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo!')

