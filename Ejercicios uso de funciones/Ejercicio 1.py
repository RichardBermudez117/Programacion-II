import math
def area_perimetro_rectangulo(base,altura):
    perimetro=2*base+ 2*altura
    area=base*altura
    return perimetro, area
bas=float(input("ingrese la base del rectangulo: "))
alt=float(input("ingrese la altura del rectangulo: "))
perimetro,area=area_perimetro_rectangulo(bas,alt)
print("perimetro", perimetro,"area",area)
