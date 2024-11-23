# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color, precio, placa):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.placa = placa

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Placa: {self.placa}"

    def editar_info(self, marca=None, modelo=None, color=None, precio=None, placa=None):
        if marca:
            self.marca = marca
        if modelo:
            self.modelo = modelo
        if color:
            self.color = color
        if precio is not None:
            self.precio = precio
        if placa:
            self.placa = placa

    def borrar_info(self):
        return f"Vehículo con placa {self.placa} eliminado."


# Subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, precio, placa, num_puertas, tipo_motor):
        super().__init__(marca, modelo, color, precio, placa)
        self.num_puertas = num_puertas
        self.tipo_motor = tipo_motor

    def mostrar_info(self):
        return super().mostrar_info() + f", Número de Puertas: {self.num_puertas}, Tipo de Motor: {self.tipo_motor}"

    def calcular_impuesto(self):
        impuesto = self.precio * 0.10  # Ejemplo: 10% del precio
        return f"Impuesto a pagar: ${impuesto:.2f}"

    def es_economico(self):
        return self.precio < 15000  # Un auto es económico si su precio es menor a 15000


# Subclase Camioneta
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, color, precio, placa, capacidad_carga, traccion):
        super().__init__(marca, modelo, color, precio, placa)
        self.capacidad_carga = capacidad_carga
        self.traccion = traccion

    def mostrar_info(self):
        return super().mostrar_info() + f", Capacidad de Carga: {self.capacidad_carga} kg, Tracción: {self.traccion}"

    def verificar_capacidad(self):
        return self.capacidad_carga > 1000  # Verifica si la capacidad es alta

    def es_4x4(self):
        return self.traccion == "4x4"  # Verifica si tiene tracción 4x4


# Subclase Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, precio, placa, capacidad_carga, tipo_combustible):
        super().__init__(marca, modelo, color, precio, placa)
        self.capacidad_carga = capacidad_carga
        self.tipo_combustible = tipo_combustible

    def mostrar_info(self):
        return super().mostrar_info() + f", Capacidad de Carga: {self.capacidad_carga} toneladas, Combustible: {self.tipo_combustible}"

    def costo_mantenimiento(self):
        return f"Costo estimado de mantenimiento: ${self.precio * 0.05:.2f}"  # Ejemplo: 5% del precio

    def necesita_licencia_especial(self):
        return self.capacidad_carga > 3  # Verifica si necesita licencia especial


# Subclase Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, precio, placa, cilindrada, tipo_moto):
        super().__init__(marca, modelo, color, precio, placa)
        self.cilindrada = cilindrada
        self.tipo_moto = tipo_moto

    def mostrar_info(self):
        return super().mostrar_info() + f", Cilindrada: {self.cilindrada} cc, Tipo de Moto: {self.tipo_moto}"

    def es_deportiva(self):
        return self.tipo_moto == "Deportiva"  # Verifica si la moto es deportiva

    def calcular_seguro(self):
        return f"Costo del seguro: ${self.precio * 0.07:.2f}"  # Ejemplo: 7% del precio


# Clase para gestionar el concesionario
class Concesionario:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            return "No hay vehículos en el concesionario."
        return "\n".join([v.mostrar_info() for v in self.vehiculos])

    def buscar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                return v.mostrar_info()
        return "Vehículo no encontrado."

    def editar_vehiculo(self, placa, **kwargs):
        for v in self.vehiculos:
            if v.placa == placa:
                v.editar_info(**kwargs)
                return f"Vehículo con placa {placa} ha sido editado."
        return "Vehículo no encontrado."

    def eliminar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                self.vehiculos.remove(v)
                return f"Vehículo con placa {placa} eliminado."
        return "Vehículo no encontrado."


# Función para interactuar con el menú
def menu_concesionario():
    concesionario = Concesionario()

    while True:
        print("\n--- Menú del Concesionario ---")
        print("1. Agregar Vehículo")
        print("2. Mostrar Vehículos")
        print("3. Buscar Vehículo por Placa")
        print("4. Editar Vehículo")
        print("5. Eliminar Vehículo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de Vehículo (Automovil, Camioneta, Camion, Moto): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            precio = float(input("Precio: "))
            placa = input("Placa: ")

            if tipo.lower() == "automovil":
                num_puertas = int(input("Número de Puertas: "))
                tipo_motor = input("Tipo de Motor: ")
                vehiculo = Automovil(marca, modelo, color, precio, placa, num_puertas, tipo_motor)

            elif tipo.lower() == "camioneta":
                capacidad_carga = float(input("Capacidad de Carga (kg): "))
                traccion = input("Tracción (4x2, 4x4): ")
                vehiculo = Camioneta(marca, modelo, color, precio, placa, capacidad_carga, traccion)

            elif tipo.lower() == "camion":
                capacidad_carga = float(input("Capacidad de Carga (toneladas): "))
                tipo_combustible = input("Tipo de Combustible: ")
                vehiculo = Camion(marca, modelo, color, precio, placa, capacidad_carga, tipo_combustible)

            elif tipo.lower() == "moto":
                cilindrada = int(input("Cilindrada (cc): "))
                tipo_moto = input("Tipo de Moto (Deportiva, Urbana, Touring, etc.): ")
                vehiculo = Moto(marca, modelo, color, precio, placa, cilindrada, tipo_moto)

            concesionario.agregar_vehiculo(vehiculo)
            print("Vehículo agregado exitosamente.")

        elif opcion == "2":
            print(concesionario.mostrar_vehiculos())

        elif opcion == "3":
            placa = input("Ingrese la placa del vehículo a buscar: ")
            print(concesionario.buscar_vehiculo(placa))

        elif opcion == "4":
            placa = input("Ingrese la placa del vehículo a editar: ")
            print("Ingrese los nuevos datos (deje vacío para no cambiar):")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            precio = input("Precio: ")
            concesionario.editar_vehiculo(placa, marca=marca or None, modelo=modelo or None,
                                           color=color or None, precio=float(precio) if precio else None)

        elif opcion == "5":
            placa = input("Ingrese la placa del vehículo a eliminar: ")
            print(concesionario.eliminar_vehiculo(placa))

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu_concesionario()
