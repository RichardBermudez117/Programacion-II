# Diccionario inicial de palabras
traductor_es_en = {
    'auto': 'car',
    'azul': 'blue',
    'red': 'network',
    'volar': 'fly',
    'blanco': 'white',
    'casa': 'house',
    'clase': 'class',
    'futbol': 'soccer',
    'hora': 'hour',
    'cama': 'bed'
}

traductor_en_es = {
    'car': 'auto',
    'blue': 'azul',
    'network': 'red',
    'fly': 'volar',
    'white': 'blanco',
    'house': 'casa',
    'class': 'clase',
    'soccer': 'futbol',
    'hour': 'hora',
    'bed': 'cama'
}

# Función para buscar una palabra en el diccionario
def buscar_palabra(traductor, idioma_origen, idioma_destino):
    palabra = input(f"Ingrese la palabra en {idioma_origen}: ").lower()
    if palabra in traductor:
        print(f"La traducción de '{palabra}' en {idioma_destino} es: {traductor[palabra]}")
    else:
        print(f"La palabra '{palabra}' no está registrada en la base de datos.")
        agregar_palabra(traductor, palabra, idioma_origen, idioma_destino)

# Función para agregar una palabra al diccionario
def agregar_palabra(traductor, palabra, idioma_origen, idioma_destino):
    nueva_traduccion = input(f"Ingrese la traducción de '{palabra}' en {idioma_destino}: ").lower()
    traductor[palabra] = nueva_traduccion
    print(f"La palabra '{palabra}' y su traducción '{nueva_traduccion}' han sido agregadas.")

# Función para eliminar una palabra del diccionario
def eliminar_palabra(traductor):
    palabra = input("Ingrese la palabra que desea eliminar: ").lower()
    if palabra in traductor:
        del traductor[palabra]
        print(f"La palabra '{palabra}' ha sido eliminada del diccionario.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

# Función para editar una palabra en el diccionario
def editar_palabra(traductor, idioma_origen, idioma_destino):
    palabra = input(f"Ingrese la palabra en {idioma_origen} que desea editar: ").lower()
    if palabra in traductor:
        nueva_traduccion = input(f"Ingrese la nueva traducción de '{palabra}' en {idioma_destino}: ").lower()
        traductor[palabra] = nueva_traduccion
        print(f"La palabra '{palabra}' ha sido actualizada con la nueva traducción '{nueva_traduccion}'.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

# Menú principal
def menu():
    while True:
        print("\n*** Traductor ***")
        print("1. Traducir de Español a Inglés")
        print("2. Traducir de Inglés a Español")
        print("3. Agregar palabra")
        print("4. Eliminar palabra")
        print("5. Editar palabra")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            buscar_palabra(traductor_es_en, 'Español', 'Inglés')
        elif opcion == "2":
            buscar_palabra(traductor_en_es, 'Inglés', 'Español')
        elif opcion == "3":
            idioma = input("¿Desea agregar palabra en Español (es) o Inglés (en)? ").lower()
            if idioma == "es":
                palabra = input("Ingrese la palabra en Español: ").lower()
                agregar_palabra(traductor_es_en, palabra, 'Español', 'Inglés')
            elif idioma == "en":
                palabra = input("Ingrese la palabra en Inglés: ").lower()
                agregar_palabra(traductor_en_es, palabra, 'Inglés', 'Español')
            else:
                print("Idioma no válido.")
        elif opcion == "4":
            idioma = input("¿Desea eliminar palabra en Español (es) o Inglés (en)? ").lower()
            if idioma == "es":
                eliminar_palabra(traductor_es_en)
            elif idioma == "en":
                eliminar_palabra(traductor_en_es)
            else:
                print("Idioma no válido.")
        elif opcion == "5":
            idioma = input("¿Desea editar palabra en Español (es) o Inglés (en)? ").lower()
            if idioma == "es":
                editar_palabra(traductor_es_en, 'Español', 'Inglés')
            elif idioma == "en":
                editar_palabra(traductor_en_es, 'Inglés', 'Español')
            else:
                print("Idioma no válido.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
menu()
