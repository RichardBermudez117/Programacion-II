import math

a=float(input("por favor ingresar un numero"))
b=float(input("por favor ingresar un numero"))
c=float(input("por favor ingresar un numero"))

r=((b**2)-4*a*c)

if(r==0):
    z=-b/2*a
    print(f"la raiz es: {z} porque es real e iguales")
if(r>0):
    z1=-b-math.sqrt(r)
    z2=-b+math.sqrt(r)

    print(f"las raices: {z1} y {z2} son reales pero distintas")
else:
    z1=-b-math.sqrt(-r)
    z2=-b+math.sqrt(-r)
    print(f"las raices: {z1}j y {z2}j son complejos o imaginarios")   
        

