def calcular_medias(n, notas, creditos):
    # Calcular media aritmética
    media_aritmetica = sum(notas) / n

    # Calcular media ponderada
    suma_ponderada = sum(nota * credito for nota, credito in zip(notas, creditos))
    suma_creditos = sum(creditos)
    media_ponderada = suma_ponderada / suma_creditos

    return media_aritmetica, media_ponderada

def main():
    n = int(input("Ingrese el número de materias: "))

    notas = []
    creditos = []
    
    for _ in range(n):
        materia = input("Ingrese el nombre de la materia: ")
        credito = float(input(f"Ingrese los créditos de {materia}: "))
        nota = float(input(f"Ingrese la nota de {materia}: "))
        
        creditos.append(credito)
        notas.append(nota)
    
    media_aritmetica, media_ponderada = calcular_medias(n, notas, creditos)

    print(f"\nMedia Aritmética: {media_aritmetica:.2f}")
    print(f"Media Ponderada: {media_ponderada:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
