import math
def relacion(num1,num2):
     if a > b:
        return "True"
     elif a < b:
        return "False"
     else:
        return "Empate"
a=int(input("ingrese numero: "))
b=int(input("ingrese numero: "))
r=relacion(a,b)
print("Resultado de la comparacion",r)
