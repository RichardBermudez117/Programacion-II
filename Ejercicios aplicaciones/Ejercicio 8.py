# Diccionario para almacenar los contactos
agenda_telefonica = {}

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre y apellido del contacto: ").title()
    if nombre in agenda_telefonica:
        print(f"El contacto '{nombre}' ya existe en la agenda.")
        return
    telefono = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    
    direccion = input("Ingrese la dirección de residencia: ")
    cumpleaños = input("Ingrese la fecha de cumpleaños (DD/MM/AAAA): ")
    
    # Guardamos el contacto en el diccionario
    agenda_telefonica[nombre] = {
        "Teléfono": telefono,
        "Correo": correo,
        "Dirección": direccion,
        "Cumpleaños": cumpleaños
    }
    print(f"Contacto '{nombre}' agregado correctamente.")

# Función para editar un contacto
def editar_contacto():
    nombre = input("Ingrese el nombre y apellido del contacto que desea editar: ").title()
    if nombre in agenda_telefonica:
        print(f"Editando contacto '{nombre}'. Deje en blanco los campos que no desea cambiar.")
        telefono = input(f"Teléfono actual ({agenda_telefonica[nombre]['Teléfono']}): ") or agenda_telefonica[nombre]['Teléfono']
        correo = input(f"Correo actual ({agenda_telefonica[nombre]['Correo']}): ") or agenda_telefonica[nombre]['Correo']
        direccion = input(f"Dirección actual ({agenda_telefonica[nombre]['Dirección']}): ") or agenda_telefonica[nombre]['Dirección']
        cumpleaños = input(f"Cumpleaños actual ({agenda_telefonica[nombre]['Cumpleaños']}): ") or agenda_telefonica[nombre]['Cumpleaños']
        
        # Actualizamos los datos del contacto
        agenda_telefonica[nombre] = {
            "Teléfono": telefono,
            "Correo": correo,
            "Dirección": direccion,
            "Cumpleaños": cumpleaños
        }
        print(f"Contacto '{nombre}' actualizado correctamente.")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre y apellido del contacto que desea eliminar: ").title()
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")

# Función para mostrar todos los contactos
def mostrar_contactos():
    if not agenda_telefonica:
        print("La agenda está vacía.")
    else:
        print("\n--- Lista de Contactos ---")
        for nombre, datos in agenda_telefonica.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {datos['Teléfono']}")
            print(f"Correo: {datos['Correo']}")
            print(f"Dirección: {datos['Dirección']}")
            print(f"Cumpleaños: {datos['Cumpleaños']}")
            print("---------------------------")
        print(f"Total de contactos: {len(agenda_telefonica)}")

# Función principal que controla el menú de la agenda
def menu():
    while True:
        print("\n--- Agenda Telefónica ---")
        print("1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            editar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            mostrar_contactos()
        elif opcion == "5":
            print("Saliendo de la agenda telefónica.")
            mostrar_contactos()  # Mostrar la lista final con la cantidad de contactos
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
