# Lista de contactos (nombre, apellido, DNI, dirección, teléfono)
contactos = [
    ["Juan", "Pérez", "12345678", "Calle Falsa 123", "555-1234"],
    ["María", "Gómez", "87654321", "Avenida Siempre Viva 456", "555-5678"],
    ["Pedro", "Ramírez", "12398745", "Calle 42", "555-9876"]
]

# Función para visualizar los contactos
def visualizar_contactos(contactos):
    print(f"{'Nombre':<10} {'Apellido':<10} {'DNI':<10} {'Dirección':<25} {'Teléfono':<10}")
    print("=" * 65)
    for contacto in contactos:
        nombre, apellido, dni, direccion, telefono = contacto
        print(f"{nombre:<10} {apellido:<10} {dni:<10} {direccion:<25} {telefono:<10}")

# Función para editar dirección y teléfono
def editar_contacto(contactos):
    dni = input("Ingrese el DNI del contacto que desea editar: ")
    
    # Buscar el contacto por DNI
    for contacto in contactos:
        if contacto[2] == dni:  # Si se encuentra el DNI
            print(f"Contacto encontrado: {contacto[0]} {contacto[1]} - Dirección: {contacto[3]}, Teléfono: {contacto[4]}")
            
            # Solicitar nueva dirección y teléfono
            nueva_direccion = input("Ingrese la nueva dirección: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            
            # Actualizar los datos
            contacto[3] = nueva_direccion
            contacto[4] = nuevo_telefono
            
            print(f"Los datos de {contacto[0]} {contacto[1]} han sido actualizados exitosamente.")
            return
    
    # Si no se encuentra el DNI
    print(f"No se encontró un contacto con el DNI {dni}.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Visualizar contactos")
        print("2. Editar dirección y teléfono")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            visualizar_contactos(contactos)
        elif opcion == "2":
            editar_contacto(contactos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el menú
menu()
