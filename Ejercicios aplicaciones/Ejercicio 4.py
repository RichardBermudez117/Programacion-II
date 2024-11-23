# Función para llenar la lista con números ingresados por el usuario
def llenar_lista():
    lista = []
    while True:
        try:
            numero = input("Ingrese un número (o 'q' para finalizar): ")
            if numero.lower() == 'q':  # Si el usuario ingresa 'q', terminar el ingreso
                break
            else:
                lista.append(int(numero))  # Agregar el número a la lista
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    return lista

# Función para separar los números en pares e impares
def separar_pares_impares(lista):
    lista.sort()  # Ordenar la lista
    pares = [num for num in lista if num % 2 == 0]  # Números pares
    impares = [num for num in lista if num % 2 != 0]  # Números impares
    return pares, impares

# Función principal
def main():
    print("Ingrese números para llenar la lista. Escriba 'q' para finalizar.")
    
    # Llenar la lista
    lista = llenar_lista()
    
    # Separar en pares e impares si la lista no está vacía
    if lista:
        pares, impares = separar_pares_impares(lista)
        print("\nLista original ordenada:", lista)
        print("Lista de números pares:", pares)
        print("Lista de números impares:", impares)
    else:
        print("No se ingresaron números.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
