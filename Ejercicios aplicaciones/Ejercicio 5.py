# Función para sumar todos los números de la lista
def sumar(lista):
    return sum(lista)  # Usamos la función sum() para sumar los elementos de la lista

# Función para multiplicar todos los números de la lista
def multiplicar(lista):
    producto_total = 1
    for numero in lista:
        producto_total *= numero  # Multiplicamos cada número en la lista
    return producto_total

# Lista de números
numeros = []

# Función del menú interactivo
def menu():
    while True:
        # Submenú de opciones
        print("\nOpciones:")
        print("1. Agregar números")
        print("2. Sumar números")
        print("3. Multiplicar números")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            agregar_numeros()  # Función para agregar números
        elif opcion == "2":
            if numeros:
                suma = sumar(numeros)
                print(f"La suma de {numeros} es: {suma}")
                menu()
            else:
                print("No hay números en la lista para sumar.")
                menu()
        elif opcion == "3":
            if numeros:
                producto = multiplicar(numeros)
                print(f"El producto de {numeros} es: {producto}")
                menu()
            else:
                print("No hay números en la lista para multiplicar.")
                menu()
        elif opcion == "4":
            print("Saliendo del programa.")
            exit()
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")
            menu()

# Función para agregar números a la lista
def agregar_numeros():
    while True:
        try:
            a = int(input("Ingrese un número (o '0' para finalizar la entrada): "))
            if a == 0:
                break  # Salir del ciclo si el usuario ingresa 0
            numeros.append(a)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Ejecutar el menú
menu()
