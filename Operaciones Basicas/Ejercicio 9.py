import math

print('por favor dar los catetos y hipotenusa del triangulo')

a=float(input('cateto opuesto:'))
b=float(input('cateto adyacente:'))
c=float(input('hipotenusa:'))

p=float(a+b+c)

print('el perimetro de ese triangulo es: ',round(p,2))

A=1/2*float(b+a)

print('el area del triangulo es: ',round(A,2))
