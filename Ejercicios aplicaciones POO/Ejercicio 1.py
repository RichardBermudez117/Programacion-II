import re

class Agenda():
    def __init__(self):
        self.contactos = []

    def Buscar(self):
        a = input("Ingresa Nombre: ")
        encontrado = False  # Variable para llevar el seguimiento del estado de búsqueda
        
        for i in self.contactos:
            if a == i[1]:  # Comprobar el nombre en la segunda posición
                print(f"{a} se encuentra en la lista.")
                encontrado = True
                break  # Salir del bucle si se encuentra
       
        if not encontrado:
            print(f"{a} no se encuentra en la lista.")
        
        self.Menu()  # Volver al menú después de la búsqueda

    def Lista(self):
        if self.contactos:
            print("Lista de Contactos:")
            for idx, elem in enumerate(self.contactos, start=1):
                print(f"{idx}. Nombre: {elem[1]}, Teléfono: {elem[2]}, Correo: {elem[3]}")
        else:
            print("La lista está vacía.")
        self.Menu()  # Volver al menú después de mostrar la lista
        
    def Añadir(self):
        a = input("Ingresar el nombre: ")
        b = input("Ingresar el número telefónico: ")
        
        # Validar que el número telefónico sea un número entero
        if not b.isdigit():
            print("El número telefónico debe ser solo dígitos.")
            self.Añadir()
            return
        
        c = input("Ingresar el correo electrónico: ")
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.match(patron, c):
            self.contactos.append(["Nombre", a, "Teléfono", b, "Correo", c])
            print("Datos agregados exitosamente.")
        else:
            if not re.match(patron_correo, c):
                print("Correo electrónico incorrecto.")
                self.Añadir()  # Volver a intentar la adición
            if not re.match(patron_telefono, b):
                print("Número telefónico incorrecto. Debe contener exactamente 10 dígitos.")
            self.Añadir()  # Volver a intentar la adición
        self.Menu()  # Volver al menú

    def Editar(self):
        a = input("Ingresar el Nombre del contacto a editar: ")
        encontrado = False  # Variable para verificar si el contacto fue encontrado
        
        for idx, contacto in enumerate(self.contactos):
            if a == contacto[1]:  # Buscar por nombre
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo número telefónico: ")
                nuevo_correo = input("Nuevo correo electrónico: ")
                
                # Validar el correo electrónico
                if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', nuevo_correo):
                    self.contactos[idx] = ["Nombre", nuevo_nombre, "Teléfono", nuevo_telefono, "Correo", nuevo_correo]
                    print(f"Contacto '{a}' editado con éxito.")
                    encontrado = True
                else:
                    print("Correo electrónico incorrecto.")
                break  # Salir del bucle si se encuentra el contacto
        
        if not encontrado:
            print(f"El contacto '{a}' no se encuentra en la lista.")
        
        self.Menu()  # Volver al menú

    def Eliminar(self):
        a = input("Ingresar el Nombre del contacto a eliminar: ")
        encontrado = False  # Variable para verificar si el contacto fue encontrado
        
        for i in self.contactos:
            if a == i[1]:  # Buscar por nombre
                self.contactos.remove(i)
                print(f"Contacto '{a}' eliminado de la lista.")
                encontrado = True
                break  # Salir del bucle si se encuentra
        
        if not encontrado:
            print(f"El contacto '{a}' no se encuentra en la lista.")
        
        self.Menu()  # Volver al menú

    def Menu(self):
        print("""\nMenú
                 1. Añadir contacto
                 2. Lista de contactos
                 3. Buscar contacto
                 4. Editar contacto
                 5. Eliminar contacto
                 6. Cerrar agenda""")
        try:
            a = int(input("Ingresar opción: "))
            if a == 1:
                self.Añadir()
            elif a == 2:
                self.Lista()
            elif a == 3:
                self.Buscar()
            elif a == 4:
                self.Editar()
            elif a == 5:
                self.Eliminar()
            elif a == 6:
                exit()
            else:
                print("Opción no válida. Intenta de nuevo.")
                self.Menu()  # Volver al menú si la opción es inválida
        except ValueError:
            print("Por favor, ingresa un número válido.")
            self.Menu()  # Volver al menú si hay un error de entrada

# Crear instancia de Agenda y mostrar el menú
nombre1 = Agenda()
nombre1.Menu()

