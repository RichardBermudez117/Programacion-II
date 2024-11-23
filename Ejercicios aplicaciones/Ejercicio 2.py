# Tupla con los meses del año
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# Función principal
def mostrar_mes():
    while True:
        try:
            # Solicitar un número al usuario
            numero = int(input("Ingrese un número del 1 al 12 para ver el mes correspondiente (o 0 para salir): "))
            
            # Si el número es 0, salir del programa
            if numero == 0:
                print("Saliendo del programa.")
                break
            
            # Verificar que el número esté en el rango válido
            if 1 <= numero <= len(meses):
                print(f"El mes correspondiente al número {numero} es {meses[numero - 1]}.")
            else:
                print("Error: el número debe estar entre 1 y 12.")
        
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

# Ejecutar el programa
mostrar_mes()
