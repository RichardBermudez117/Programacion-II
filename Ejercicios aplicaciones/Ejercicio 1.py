# Base de datos de contactos usando tuplas
contactos = [
    ("Juan", "Pérez", "12345678", "Calle Falsa 123", "555-1234"),
    ("María", "Gómez", "87654321", "Avenida Siempre Viva 456", "555-5678"),
    ("Pedro", "Ramírez", "12398745", "Calle 42", "555-9876")
]

# Función para visualizar los contactos
def visualizar_contactos(contactos):
    if len(contactos) == 0:
        print("No hay contactos en la base de datos.")
    else:
        print(f"{'Nombre':<10} {'Apellido':<10} {'DNI':<10} {'Dirección':<25} {'Teléfono':<10}")
        print("=" * 65)
        for contacto in contactos:
            nombre, apellido, dni, direccion, telefono = contacto
            print(f"{nombre:<10} {apellido:<10} {dni:<10} {direccion:<25} {telefono:<10}")
visualizar_contactos(contactos)
