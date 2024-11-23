# Clase base Animal
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg"


# Clase Terrestre
class Terrestre(Animal):
    def __init__(self, nombre, edad, peso, tipo_patas, velocidad):
        super().__init__(nombre, edad, peso)
        self.tipo_patas = tipo_patas
        self.velocidad = velocidad

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Tipo de patas: {self.tipo_patas}, Velocidad: {self.velocidad} km/h"


# Clase Aéreo
class Aereo(Animal):
    def __init__(self, nombre, edad, peso, envergadura_alas, altura_vuelo):
        super().__init__(nombre, edad, peso)
        self.envergadura_alas = envergadura_alas
        self.altura_vuelo = altura_vuelo

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Envergadura de alas: {self.envergadura_alas} m, Altura de vuelo: {self.altura_vuelo} m"


# Clase Acuático
class Acuatico(Animal):
    def __init__(self, nombre, edad, peso, tipo_agua, velocidad_nado):
        super().__init__(nombre, edad, peso)
        self.tipo_agua = tipo_agua
        self.velocidad_nado = velocidad_nado

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Tipo de agua: {self.tipo_agua}, Velocidad de nado: {self.velocidad_nado} km/h"


# Función para ingresar un animal
def ingresar_animal():
    print("¿Qué tipo de animal desea ingresar?")
    print("1. Terrestre")
    print("2. Aéreo")
    print("3. Acuático")
    
    opcion = int(input("Seleccione una opción: "))

    nombre = input("Ingrese el nombre del animal: ")
    edad = int(input("Ingrese la edad del animal: "))
    peso = float(input("Ingrese el peso del animal en kg: "))

    if opcion == 1:
        tipo_patas = input("Ingrese el tipo de patas: ")
        velocidad = float(input("Ingrese la velocidad del animal en km/h: "))
        animal = Terrestre(nombre, edad, peso, tipo_patas, velocidad)
    elif opcion == 2:
        envergadura_alas = float(input("Ingrese la envergadura de las alas en metros: "))
        altura_vuelo = float(input("Ingrese la altura máxima de vuelo en metros: "))
        animal = Aereo(nombre, edad, peso, envergadura_alas, altura_vuelo)
    elif opcion == 3:
        tipo_agua = input("¿Es un animal de agua dulce o salada?: ")
        velocidad_nado = float(input("Ingrese la velocidad de nado en km/h: "))
        animal = Acuatico(nombre, edad, peso, tipo_agua, velocidad_nado)
    else:
        print("Opción no válida")
        return None

    return animal


# Función principal
def main():
    zoologico = []

    while True:
        print("\n--- Registro de Animales en el Zoológico ---")
        animal = ingresar_animal()

        if animal:
            zoologico.append(animal)
            print("\nAnimal registrado exitosamente.")
            print(animal.mostrar_informacion())

        continuar = input("\n¿Desea ingresar otro animal? (s/n): ").lower()
        if continuar != 's':
            break

    print("\n--- Animales Registrados ---")
    for a in zoologico:
        print(a.mostrar_informacion())


if __name__ == "__main__":
    main()
