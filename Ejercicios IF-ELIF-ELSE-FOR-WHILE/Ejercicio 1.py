print("Por favor ingresar el nombre,apellidos,documento de identidad y sueldo")
a=input("Nombre y Apellidos: ")
b=int(input("Documento de identidad: "))
c=int(input("Sueldo: "))
if(c>1380606 ):
    print("Nombre y Apellidos:{a} "
          "Documento de identidad:{b} "
          "Sueldo:{c} el sueldo es superior al minimo")
else:
    print(f"Nombre y Apellidos:{a} "
          f"Documento de identidad:{b} "
          f"Sueldo:{c} el sueldo es inferior al minimo")
