# Clase principal Persona
class Persona:
    def __init__(self, codigo, apellidos, nombres, documento, area, hora_ingreso, temp_ingreso, hora_salida=None, temp_salida=None):
        self.codigo = codigo
        self.apellidos = apellidos
        self.nombres = nombres
        self.documento = documento
        self.area = area  # seguridad, servicios generales, administrativo, auxiliar o visitante
        self.hora_ingreso = hora_ingreso
        self.temp_ingreso = temp_ingreso
        self.hora_salida = hora_salida
        self.temp_salida = temp_salida

    def mostrar_informacion(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombres} {self.apellidos}")
        print(f"Documento: {self.documento}")
        print(f"Área: {self.area}")
        print(f"Hora de ingreso: {self.hora_ingreso}")
        print(f"Temperatura de ingreso: {self.temp_ingreso} °C")
        if self.hora_salida:
            print(f"Hora de salida: {self.hora_salida}")
            print(f"Temperatura de salida: {self.temp_salida} °C")
        print("-" * 40)

    def editar_informacion(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print(f"Información de {self.nombres} {self.apellidos} actualizada.")

# Clase Empresa para gestionar empleados y visitantes
class Empresa:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)
        print(f"Persona {persona.nombres} {persona.apellidos} agregada con éxito.")

    def eliminar_persona(self, codigo):
        for persona in self.personas:
            if persona.codigo == codigo:
                self.personas.remove(persona)
                print(f"Persona con código {codigo} eliminada.")
                return
        print(f"Persona con código {codigo} no encontrada.")

    def buscar_por_codigo(self, codigo):
        for persona in self.personas:
            if persona.codigo == codigo:
                return persona
        print(f"Persona con código {codigo} no encontrada.")
        return None

    def mostrar_por_criterio(self, criterio):
        if criterio == "temperatura alta":
            print("\nPersonas con temperatura mayor a 37.5°C:")
            for persona in self.personas:
                if persona.temp_ingreso > 37.5 or (persona.temp_salida and persona.temp_salida > 37.5):
                    persona.mostrar_informacion()

        elif criterio == "cargo":
            cargo = input("Ingrese el cargo (seguridad, servicios generales, administrativo, auxiliar, visitante): ").lower()
            print(f"\nPersonas en el área de {cargo}:")
            for persona in self.personas:
                if persona.area.lower() == cargo:
                    persona.mostrar_informacion()

        elif criterio == "hora llegada":
            hora = input("Ingrese la hora de llegada (HH:MM): ")
            print(f"\nPersonas que ingresaron a las {hora}:")
            for persona in self.personas:
                if persona.hora_ingreso == hora:
                    persona.mostrar_informacion()

        elif criterio == "hora salida":
            hora = input("Ingrese la hora de salida (HH:MM): ")
            print(f"\nPersonas que salieron a las {hora}:")
            for persona in self.personas:
                if persona.hora_salida == hora:
                    persona.mostrar_informacion()

    def verificar_alertas(self):
        for persona in self.personas:
            if persona.temp_ingreso > 38 or (persona.temp_salida and persona.temp_salida > 38):
                print(f"ALERTA: {persona.nombres} {persona.apellidos} tiene una temperatura superior a 38°C.")

# Función para el menú de interacción
def menu():
    empresa = Empresa()
    
    while True:
        print("\n=== Menú de la Empresa ===")
        print("1. Agregar persona")
        print("2. Editar información de persona")
        print("3. Eliminar persona")
        print("4. Buscar persona por código")
        print("5. Mostrar personas por criterio")
        print("6. Verificar alertas de temperatura")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar persona
            codigo = input("Ingrese el código: ")
            apellidos = input("Ingrese los apellidos: ")
            nombres = input("Ingrese los nombres: ")
            documento = input("Ingrese el número de documento: ")
            area = input("Ingrese el área (seguridad, servicios generales, administrativo, auxiliar o visitante): ").lower()
            hora_ingreso = input("Ingrese la hora de ingreso (HH:MM): ")
            temp_ingreso = float(input("Ingrese la temperatura de ingreso (°C): "))

            persona = Persona(codigo, apellidos, nombres, documento, area, hora_ingreso, temp_ingreso)
            empresa.agregar_persona(persona)

        elif opcion == "2":
            # Editar información
            codigo = input("Ingrese el código de la persona a editar: ")
            persona = empresa.buscar_por_codigo(codigo)
            if persona:
                print("Deje en blanco si no desea cambiar un campo.")
                nuevos_datos = {}
                nuevos_datos["apellidos"] = input(f"Nuevo apellido ({persona.apellidos}): ") or persona.apellidos
                nuevos_datos["nombres"] = input(f"Nuevo nombre ({persona.nombres}): ") or persona.nombres
                nuevos_datos["documento"] = input(f"Nuevo documento ({persona.documento}): ") or persona.documento
                nuevos_datos["area"] = input(f"Nueva área ({persona.area}): ") or persona.area
                nuevos_datos["hora_ingreso"] = input(f"Nueva hora de ingreso ({persona.hora_ingreso}): ") or persona.hora_ingreso
                nuevos_datos["temp_ingreso"] = input(f"Nueva temperatura de ingreso ({persona.temp_ingreso}°C): ") or persona.temp_ingreso
                nuevos_datos["hora_salida"] = input(f"Nueva hora de salida ({persona.hora_salida}): ") or persona.hora_salida
                nuevos_datos["temp_salida"] = input(f"Nueva temperatura de salida ({persona.temp_salida}°C): ") or persona.temp_salida
                persona.editar_informacion(**nuevos_datos)

        elif opcion == "3":
            # Eliminar persona
            codigo = input("Ingrese el código de la persona a eliminar: ")
            empresa.eliminar_persona(codigo)

        elif opcion == "4":
            # Buscar por código
            codigo = input("Ingrese el código de la persona a buscar: ")
            persona = empresa.buscar_por_codigo(codigo)
            if persona:
                persona.mostrar_informacion()

        elif opcion == "5":
            # Mostrar por criterio
            print("\nCriterios de búsqueda:")
            print("1. Temperatura mayor a 37.5°C")
            print("2. Cargo dentro de la empresa")
            print("3. Hora de llegada")
            print("4. Hora de salida")
            criterio = input("Seleccione un criterio (1-4): ")

            if criterio == "1":
                empresa.mostrar_por_criterio("temperatura alta")
            elif criterio == "2":
                empresa.mostrar_por_criterio("cargo")
            elif criterio == "3":
                empresa.mostrar_por_criterio("hora llegada")
            elif criterio == "4":
                empresa.mostrar_por_criterio("hora salida")

        elif opcion == "6":
            # Verificar alertas de temperatura
            empresa.verificar_alertas()

        elif opcion == "7":
            print("Saliendo del programa.")
            exit()

        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()


