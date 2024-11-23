import random as r
import getpass
a="si"
while a=="si":
    print("""PIEDRA PAPEL O TIJERA
                    1.  Contra la maquina
                    2.  Multijugador
                    """)
    a=input("elegir opcion: ")
    if(a=="1"):
        a="si"
        while a=="si":
            print("""ELECCIONES
                        1.  Piedra
                        2.  Papel
                        3.  Tijera
                        """)
            b=r.randint(1,3)
            a=int(input("seleccionar jugada: "))
            if(a==b):
                print("empate")
            elif(a==1 and b==2):
                print("gana la computadora")
            elif(a==2 and b==3):
                print("gana la computadora")
            elif(a==2 and b==1):
                print("gana el jugador")
            elif(a==1 and b==3):
                print("gana el jugador")
            a=input("desea jugar denuevo: si o no?: ")
        else:
             print("programa terminado... Fin")
    elif(a=="2"):
        a="si"
        while a=="si":
            print("""ELECCIONES
                        1.  Piedra
                        2.  Papel
                        3.  Tijera
                        """)
            a=int(input("seleccionar jugada jugador 1: "))
            b=int(input("seleccionar jugada jugador 2: "))
            if(a==b):
                print("empate")
            elif(a==1 and b==2):
                print("gana el jugador 2")
            elif(a==2 and b==3):
                print("gana el jugador 2")
            elif(a==2 and b==1):
                print("gana el jugador 1")
            elif(a==1 and b==3):
                print("gana el jugador 1")
            a=input("desea jugar denuevo: si o no?: ")
        else:
             print("programa terminado... Fin")
            

