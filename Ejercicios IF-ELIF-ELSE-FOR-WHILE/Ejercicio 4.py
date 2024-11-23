import math
while True:
    print("""CALCULADORA
             1. SUMA
             2. RESTA
             3. PRODUCTO
             4. COCIENTE
             5. PORCENTAJES
             6. COMPARACION PARES E IMPARES
             7. TRIGONOMETRIA
             """)
    a=input("cual opcion necesitas: ")

    if(a=="1"):
        L=float(input("ingresar dato numerico: "))
        Z=float(input("ingresar dato numerico: "))
        T=L + Z
        print(f"la suma da {T}")
    elif(a=="2"):
        L=float(input("ingresar dato numerico: "))
        Z=float(input("ingresar dato numerico: "))
        T=L - Z
        print(f"la suma da {T}")
    elif(a=="3"):
        L=float(input("ingresar dato numerico: "))
        Z=float(input("ingresar dato numerico: "))
        T=L*Z
        print(f"la suma da {T}")
    elif(a=="4"):
        L=float(input("ingresar dato numerico: "))
        Z=float(input("ingresar dato numerico: "))
        T=L/Z
        print(f"la suma da {T}")
    elif(a=="5"):
        L=float(input("ingresar dato numerico: "))
        Z=float(input("ingresar dato numerico: "))
        T=(L/Z)*100
        print(f"la suma da {T}%")
    elif(a=="6"):
        L=float(input("ingresar dato numerico: "))
        if((L%2)==0):
            print(f"El numero es par")
        else:
            print(f"el numero es impar")
    elif(a=="7"):
        print("""                 1. coseno
                 2. seno
                 3. tangente
                 """)
        b=input("que operacion trigonometrica: ")
        if(b=="1"):
           L=float(input("ingresar dato : "))
           F= math.radians(L)
           T=math.cos(F)
           print(f"el resultado es: {T}")
        elif(b=="2"):
           L=float(input("ingresar dato : "))
           F= math.radians(L)
           T=math.sin(F)
           print(f"el resultado es: {T}")
        elif(b=="3"):
           L=float(input("ingresar dato de : "))
           F= math.radians(L)
           T=math.tan(F)
           print(f"el resultado es: {T}")
