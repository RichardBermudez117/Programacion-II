import math as m

def hallar_mayor_menor(num1,num2):
    ma=max(num1,num2)
    mi=min(num1,num2)
    return (ma,mi)
c=float(input("ingresar numero: "))
d=float(input("ingresar numero: "))
r1,r2=hallar_mayor_menor(c,d)
print("el maximo es ",r1," y el menor es ",r2)
    
