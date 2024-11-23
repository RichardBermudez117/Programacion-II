import math
l=[]
p=0
n=0
po=0
for i in range (5):
    num=int(input("ingresar 5 numeros enteros: "))
    if(i<=5):
        l.append(num)
    else:
        print("exceso de numero solo se pueden 5 numeros enteros")
for num in l:
    if(num<0):
        n += num
else:
    p += num
    po+= 1
if(po>0):
    prom=p/po
else:
    prom= 0
print(f"la suma de negativos da {n}")
print(f"el promedio de positivos es {prom}")

    


