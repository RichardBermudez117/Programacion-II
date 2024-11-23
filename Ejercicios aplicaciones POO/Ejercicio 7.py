# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.generacion = self.asignar_generacion()

    def asignar_generacion(self):
        """Determina la generación de acuerdo a la edad"""
        if self.edad >= 90:
            return "Bisabuelos"
        elif self.edad >= 60:
            return "Abuelos"
        elif self.edad >= 35:
            return "Padres"
        elif self.edad >= 18:
            return "Yo"
        else:
            return "Hijos"

    def mostrar_info(self):
        """Muestra la información de la persona"""
        return (f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad}\n"
                f"Género: {self.genero}\n"
                f"Generación: {self.generacion}\n")


# Clase Generacion para organizar a las personas por generaciones
class Generacion:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_ascendente(self):
        """Muestra las personas ordenadas de la generación más joven a la más antigua"""
        personas_ordenadas = sorted(self.personas, key=lambda x: x.edad)
        print("\n--- Árbol Genealógico (Ascendente) ---")
        for persona in personas_ordenadas:
            print(persona.mostrar_info())
            print("-" * 40)

    def mostrar_descendente(self):
        """Muestra las personas ordenadas de la generación más antigua a la más joven"""
        personas_ordenadas = sorted(self.personas, key=lambda x: x.edad, reverse=True)
        print("\n--- Árbol Genealógico (Descendente) ---")
        for persona in personas_ordenadas:
            print(persona.mostrar_info())
            print("-" * 40)


# Función para el menú de interacción
def menu():
    arbol = Generacion()

    while True:
        print("\n=== Menú del Árbol Genealógico ===")
        print("1. Agregar familiar")
        print("2. Mostrar árbol genealógico ascendente")
        print("3. Mostrar árbol genealógico descendente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar familiar
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            genero = input("Ingrese el género (M/F): ")
            persona = Persona(nombre, apellido, edad, genero)
            arbol.agregar_persona(persona)
            print(f"{nombre} {apellido} agregado al árbol genealógico.")

        elif opcion == "2":
            # Mostrar árbol ascendente
            arbol.mostrar_ascendente()

        elif opcion == "3":
            # Mostrar árbol descendente
            arbol.mostrar_descendente()

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente nuevamente.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
