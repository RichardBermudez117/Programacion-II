import math

def  Suma ():
    a=float(input("numeros: "))
    b=float(input("numeros: "))
    print(a+b)
    menu()
def  Resta ():
    a=float(input("numeros: "))
    b=float(input("numeros: "))
    print(a-b)
    menu()
def  Multiplicacion ():
    a=float(input("numeros: "))
    b=float(input("numeros: "))
    print(a*b)
    menu()
def  Division ():
    a=float(input("numeros: "))
    b=float(input("numeros: "))
    print(a/b)
    menu()
def  menu(): #Esta es la funcion principal
    print("""Seleccion: 1: Suma
                                       2: Resta
                                       3: Multiplicacion
                                       4: Division
                                       5: salir""")
    op=int(input("Opcion deseada: "))
    while op>=1 and op<=5:
        if op == 1:
            Suma()
        elif op == 2:
            Resta()
        elif op ==3:
            Multiplicacion()
        elif op ==4:
            Division()
        elif op==5:
            exit()
        else:
            print("error")
menu()
