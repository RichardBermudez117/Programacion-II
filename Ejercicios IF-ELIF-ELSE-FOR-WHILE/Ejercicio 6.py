import math

print("""SELECCION DE CANDIDATOS PRESIDENCIALES
                1. Alvaro Uribe Velez
                2. Gustavo Petro
                3. Miguel Abraham Polo Polo
                4. Vikhy Avila Geneco
                5. Voto en blanco
                """)
a=input("Por favor seleccionar una opcion: ")
if (a== "1"):
    print("Usted a votado por el candidato Uribe")
elif (a== "2"):
    print("Usted a votado por el candidato Petro")
elif (a== "3"):
    print("Usted a votado por el candidato Polo Polo")
elif (a== "4"):
    print("Usted a votado por el candidato Geneco")
elif (a== "5"):
    print("Usted a votado por el voto en blanco")
else:
    print("opcion erronea")
