from abc import ABC, abstractmethod
import math

# Clase abstracta FiguraGeometrica
class FiguraGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

# Clase Triangulo
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Clase Circunferencia
class Circunferencia(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase Cuadrado
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Clase Rectangulo
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Clase Paralelogramo
class Paralelogramo(FiguraGeometrica):
    def __init__(self, base, altura, lado):
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.lado)

# Clase Trapecio
class Trapecio(FiguraGeometrica):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

# Clase Rombo
class Rombo(FiguraGeometrica):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Función para ingresar los datos y calcular área y perímetro
def ingresar_datos_figura():
    print("\nSeleccione la figura geométrica:")
    print("1. Triángulo")
    print("2. Circunferencia")
    print("3. Cuadrado")
    print("4. Rectángulo")
    print("5. Paralelogramo")
    print("6. Trapecio")
    print("7. Rombo")
    
    opcion = int(input("Ingrese el número de la figura: "))
    
    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        lado1 = float(input("Ingrese el primer lado del triángulo: "))
        lado2 = float(input("Ingrese el segundo lado del triángulo: "))
        lado3 = float(input("Ingrese el tercer lado del triángulo: "))
        figura = Triangulo(base, altura, lado1, lado2, lado3)
    
    elif opcion == 2:
        radio = float(input("Ingrese el radio de la circunferencia: "))
        figura = Circunferencia(radio)
    
    elif opcion == 3:
        lado = float(input("Ingrese el lado del cuadrado: "))
        figura = Cuadrado(lado)
    
    elif opcion == 4:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        figura = Rectangulo(base, altura)
    
    elif opcion == 5:
        base = float(input("Ingrese la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))
        lado = float(input("Ingrese el lado del paralelogramo: "))
        figura = Paralelogramo(base, altura, lado)
    
    elif opcion == 6:
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        lado1 = float(input("Ingrese el primer lado del trapecio: "))
        lado2 = float(input("Ingrese el segundo lado del trapecio: "))
        figura = Trapecio(base_mayor, base_menor, altura, lado1, lado2)
    
    elif opcion == 7:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        lado = float(input("Ingrese el lado del rombo: "))
        figura = Rombo(diagonal_mayor, diagonal_menor, lado)
    
    else:
        print("Opción no válida.")
        return None

    return figura

# Función principal
def main():
    while True:
        figura = ingresar_datos_figura()
        
        if figura:
            print(f"\nÁrea: {figura.calcular_area()}")
            print(f"Perímetro: {figura.calcular_perimetro()}")
        
        continuar = input("\n¿Desea ingresar otra figura? (s/n): ").lower()
        if continuar == 'si':
            main()
        else:
            exit()

if __name__ == "__main__":
    main()
