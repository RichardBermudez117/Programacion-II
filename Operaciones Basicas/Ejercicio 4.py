import math
print('por favor ingresar su peso en kilogramos y su altura en metros')
peso=input('peso:\n')
altura=input('altura:\n')

imc=float(peso)/float(altura)

print('su masa corporal es de: ',round(imc,2))
