L=[0]
a=int(input("por favor ingresar un numero entero: "))
pos=0
while a>=L[pos]:
    L.append(a)
    pos += 1
    a=int(input("por favor ingresar un numero: "))
    while a<=L[pos]:
        print("eso no es correcto")
        a=int(input("por favor ingresar un numero: "))
