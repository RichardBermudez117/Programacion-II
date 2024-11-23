import math
print('por favor ingresar la temperatura en grados farenheit')

f=input('Farenheit:')

kelvin=(float(f)-32)*(5/9)+273

print('la conversion a grados Kelvin es: ',round(kelvin,2))
