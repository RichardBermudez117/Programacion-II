import math
def area_perimetro_circulo(radio):
    perimetro=2*math.pi*rad
    area=math.pi*(rad**2)
    return perimetro, area
rad=float(input("ingrese el radio del circulo: "))
perimetro,area=area_perimetro_circulo(rad)
print("perimetro", perimetro,"area",area)
