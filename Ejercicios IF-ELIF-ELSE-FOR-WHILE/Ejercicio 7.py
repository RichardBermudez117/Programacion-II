
lista= []

n = int(input("¿Cuántos nombres de estudiantes desea ingresar?:  "))

for i in range(n):
    L = input("Ingrese el nombre del estudiante #{}: ".format (i + 1))
    lista.append(L)

while True:
    a= input("Ingrese el nombre a buscar (o escriba 'salir' para terminar): ")

    if a.lower() == 'salir':
        print("Finalizando la búsqueda.")
        break

    encontrado = False
    for L in lista:
        if L.lower() == a.lower():
            encontrado = True
            break
    
    if encontrado:
        print("El nombre '{}' está en la lista.".format(a))
    else:
        print("El nombre '{}' no está en la lista.".format(a))
