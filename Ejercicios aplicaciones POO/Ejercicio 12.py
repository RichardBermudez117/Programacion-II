import numpy as np

def obtener_resistencias(codigo_estudiante):
    # Convertir el código en una lista de enteros
    cifras = [int(digito) for digito in codigo_estudiante]
    
    # Calcular las resistencias R1, R2, R3, R4, R5
    R1 = sum(cifras[:3])  # Suma de las tres primeras cifras
    R2 = sum(cifras[1:4])  # Suma de la segunda, tercera y cuarta cifra
    R3 = sum(cifras[2:5])  # Suma de la tercera, cuarta y quinta cifra
    R4 = sum(cifras[3:6])  # Suma de la cuarta, quinta y sexta cifra
    R5 = sum(cifras[-3:])  # Suma de las tres últimas cifras

    # Reemplazar resistencias que suman cero por 10 ohmios
    resistencias = np.array([R1, R2, R3, R4, R5])
    resistencias[resistencias == 0] = 10

    return resistencias

def calcular_voltaje(codigo_estudiante):
    # Calcular Vb como la suma de las cifras del código del estudiante
    return sum(int(digito) for digito in codigo_estudiante)

def main():
    # Ingresar el código del estudiante
    codigo_estudiante = input("Ingrese su código de estudiante (6 cifras): ")

    # Validar que el código tiene 6 cifras
    if len(codigo_estudiante) != 6 or not codigo_estudiante.isdigit():
        print("El código debe tener exactamente 6 cifras numéricas.")
        main()
        return

    # Obtener las resistencias
    resistencias = obtener_resistencias(codigo_estudiante)

    # Calcular el voltaje
    Vb = calcular_voltaje(codigo_estudiante)

    # Imprimir los resultados
    print("\nResultados:")
    print(f"Tensión de la fuente de voltaje (Vb): {Vb} V")
    for i, R in enumerate(resistencias, start=1):
        print(f"R{i}: {R} ohmios")

if __name__ == "__main__":
    main()
