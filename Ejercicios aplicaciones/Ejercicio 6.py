# Función para agregar nombres a la lista
def agregar_estudiantes():
    estudiantes = []
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'q' para finalizar): ")
        if nombre.lower() == 'q':  # Salir cuando se ingresa 'q'
            break
        estudiantes.append(nombre)
    return estudiantes

# Función para buscar nombres en la lista
def buscar_estudiante(lista):
    nombre = input("Ingrese el nombre que desea buscar: ")
    if nombre in lista:
        print(f"El estudiante {nombre} está en la lista.")
    else:
        print(f"El estudiante {nombre} NO está en la lista.")

# Función principal
def main():
    print("Vamos a crear una lista de estudiantes.")
    
    # Crear la lista de estudiantes
    estudiantes = agregar_estudiantes()
    
    # Permitir buscar nombres en la lista
    if estudiantes:
        while True:
            buscar_estudiante(estudiantes)
            continuar = input("¿Desea buscar otro estudiante? (si/no): ").lower()
            if continuar != "si":
                break
    else:
        print("No se ingresaron nombres de estudiantes.")
    
    print("Programa finalizado.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
