class ConversorRomano:
    def __init__(self):
        # Mapa de números romanos y sus valores
        self.romanos = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

    def entero_a_romano(self, numero):
        if not (1 <= numero <= 3999):
            raise ValueError("El número debe estar entre 1 y 3999.")
        
        resultado = ""
        for romano, valor in self.romanos:
            while numero >= valor:
                resultado += romano
                numero -= valor
        return resultado


class ConversorEntero:
    def __init__(self):
        # Mapa de números romanos y sus valores
        self.romanos = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

    def romano_a_entero(self, romano):
        romano = romano.upper()
        resultado = 0
        i = 0
        longitud = len(romano)
        while i < longitud:
            if i + 1 < longitud and romano[i:i+2] in self.romanos:
                resultado += self.romanos[romano[i:i+2]]
                i += 2
            else:
                resultado += self.romanos[romano[i]]
                i += 1
        return resultado


def menu():
    conversor_romano = ConversorRomano()
    conversor_entero = ConversorEntero()
    
    while True:
        print("""
        Menú:
        1. Número entero a romano
        2. Número romano a entero
        3. Salir
        """)
        opcion = int(input("¿Qué opción desea?: "))

        if opcion == 1:
            numero = int(input("Ingrese un número entero (1-3999): "))
            try:
                resultado = conversor_romano.entero_a_romano(numero)
                print(f"El número {numero} en romano es: {resultado}")
            except ValueError as e:
                print(e)

        elif opcion == 2:
            romano = input("Ingrese un número romano: ")
            resultado = conversor_entero.romano_a_entero(romano)
            print(f"El número romano {romano} en entero es: {resultado}")

        elif opcion == 3:
            print("Saliendo del programa.")
            exit()

        else:
            print("Opción no válida. Intente de nuevo.")
            menu()


if __name__ == "__main__":
    menu()
