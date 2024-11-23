# Diccionario para almacenar los libros
inventario_libros = {
    "001": {"Título": "Cien años de soledad", "Autor": "Gabriel García Márquez", "Año": 1967, "Prestados": 0},
    "002": {"Título": "Don Quijote de la Mancha", "Autor": "Miguel de Cervantes", "Año": 1605, "Prestados": 0},
    "003": {"Título": "El principito", "Autor": "Antoine de Saint-Exupéry", "Año": 1943, "Prestados": 0},
    "004": {"Título": "1984", "Autor": "George Orwell", "Año": 1949, "Prestados": 0},
    "005": {"Título": "La sombra del viento", "Autor": "Carlos Ruiz Zafón", "Año": 2001, "Prestados": 0}
}

# Lista para almacenar los usuarios registrados
usuarios = []

# Variable para contar las consultas de libros
consultas_libros = 0

# Función para mostrar el inventario de libros
def mostrar_libros():
    print("\n--- Inventario de Libros ---")
    for ref, datos in inventario_libros.items():
        print(f"Número de referencia: {ref}")
        print(f"Título: {datos['Título']}")
        print(f"Autor: {datos['Autor']}")
        print(f"Año: {datos['Año']}")
        print(f"Prestados: {datos['Prestados']}")
        print("---------------------------")

# Función para buscar un libro por título o autor
def buscar_libro():
    global consultas_libros
    consulta = input("Ingrese el título o el autor del libro que desea consultar: ").title()
    encontrado = False
    
    for datos in inventario_libros.values():
        if consulta in datos["Título"] or consulta in datos["Autor"]:
            print(f"Libro encontrado: {datos['Título']} de {datos['Autor']}")
            consultas_libros += 1
            encontrado = True
            break
            
    if not encontrado:
        print("No se encontró ningún libro con esa búsqueda.")

# Función para agregar un nuevo libro
def agregar_libro():
    ref = input("Ingrese el número de referencia del nuevo libro: ")
    if ref in inventario_libros:
        print(f"Ya existe un libro con el número de referencia '{ref}'.")
        return
    
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación: "))
    
    # Guardamos el nuevo libro en el diccionario
    inventario_libros[ref] = {
        "Título": titulo,
        "Autor": autor,
        "Año": año,
        "Prestados": 0
    }
    print(f"Libro '{titulo}' agregado correctamente al inventario.")

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    usuarios.append(nombre)
    print(f"Usuario '{nombre}' registrado correctamente.")

# Función principal que controla el menú de la biblioteca
def menu():
    while True:
        print("\n--- Biblioteca ---")
        print("1. Mostrar libros")
        print("2. Buscar libro")
        print("3. Agregar libro")
        print("4. Registrar usuario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            agregar_libro()
        elif opcion == "4":
            registrar_usuario()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()

# Mostrar estadísticas finales
print(f"\nTotal de libros consultados: {consultas_libros}")
print(f"Total de usuarios registrados: {len(usuarios)}")

