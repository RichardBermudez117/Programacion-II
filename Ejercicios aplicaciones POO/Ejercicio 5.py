# Clase base para vehículos
class Vehiculo:
    def __init__(self, modelo, pintura, cantidad_inventario):
        self.modelo = modelo
        self.pintura = pintura
        self.cantidad_inventario = cantidad_inventario

    def mostrar_informacion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de pintura: {self.pintura}")
        print(f"Cantidad en inventario: {self.cantidad_inventario}")
    
    def actualizar_inventario(self, cantidad):
        self.cantidad_inventario += cantidad
        print(f"Nuevo inventario de {self.modelo}: {self.cantidad_inventario}")

# Clase Automóvil hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, modelo, pintura, cantidad_inventario, num_puertas):
        super().__init__(modelo, pintura, cantidad_inventario)
        self.num_puertas = num_puertas
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.num_puertas}")

# Clase Camioneta hereda de Vehiculo
class Camioneta(Vehiculo):
    def __init__(self, modelo, pintura, cantidad_inventario, traccion):
        super().__init__(modelo, pintura, cantidad_inventario)
        self.traccion = traccion  # 4x2, 4x4, etc.
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de tracción: {self.traccion}")

# Clase Camión hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, modelo, pintura, cantidad_inventario, capacidad_carga):
        super().__init__(modelo, pintura, cantidad_inventario)
        self.capacidad_carga = capacidad_carga  # Toneladas
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de carga: {self.capacidad_carga} toneladas")

# Clase Tractocamion hereda de Vehiculo
class Tractocamion(Vehiculo):
    def __init__(self, modelo, pintura, cantidad_inventario, num_ejes):
        super().__init__(modelo, pintura, cantidad_inventario)
        self.num_ejes = num_ejes
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de ejes: {self.num_ejes}")

# Clase Concesionario para gestionar vehículos
class Concesionario:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.modelo} agregado al inventario.")
    
    def eliminar_vehiculo(self, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                self.vehiculos.remove(vehiculo)
                print(f"Vehículo {modelo} eliminado del inventario.")
                return
        print(f"Vehículo {modelo} no encontrado.")

    def buscar_vehiculo(self, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                print(f"Vehículo {modelo} encontrado:")
                vehiculo.mostrar_informacion()
                return
        print(f"Vehículo {modelo} no encontrado.")

    def mostrar_todos_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en el inventario.")
        else:
            for vehiculo in self.vehiculos:
                vehiculo.mostrar_informacion()
                print("-" * 30)

# Función para el menú principal
def menu():
    concesionario = Concesionario()
    while True:
        print("\n=== Menú del Concesionario ===")
        print("1. Agregar vehículo")
        print("2. Buscar vehículo por modelo")
        print("3. Eliminar vehículo")
        print("4. Mostrar todos los vehículos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de vehículo (automovil, camioneta, camion, tractocamion): ").lower()
            modelo = input("Ingrese el modelo: ")
            pintura = input("Ingrese el tipo de pintura: ")
            cantidad_inventario = int(input("Ingrese la cantidad en inventario: "))

            if tipo == "automovil":
                num_puertas = int(input("Ingrese el número de puertas: "))
                vehiculo = Automovil(modelo, pintura, cantidad_inventario, num_puertas)
            elif tipo == "camioneta":
                traccion = input("Ingrese el tipo de tracción (4x2, 4x4): ")
                vehiculo = Camioneta(modelo, pintura, cantidad_inventario, traccion)
            elif tipo == "camion":
                capacidad_carga = float(input("Ingrese la capacidad de carga en toneladas: "))
                vehiculo = Camion(modelo, pintura, cantidad_inventario, capacidad_carga)
            elif tipo == "tractocamion":
                num_ejes = int(input("Ingrese el número de ejes: "))
                vehiculo = Tractocamion(modelo, pintura, cantidad_inventario, num_ejes)
            else:
                print("Tipo de vehículo no válido.")
                continue

            concesionario.agregar_vehiculo(vehiculo)

        elif opcion == "2":
            modelo = input("Ingrese el modelo del vehículo a buscar: ")
            concesionario.buscar_vehiculo(modelo)

        elif opcion == "3":
            modelo = input("Ingrese el modelo del vehículo a eliminar: ")
            concesionario.eliminar_vehiculo(modelo)

        elif opcion == "4":
            concesionario.mostrar_todos_vehiculos()

        elif opcion == "5":
            print("Saliendo del programa.")
            exit()

        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
