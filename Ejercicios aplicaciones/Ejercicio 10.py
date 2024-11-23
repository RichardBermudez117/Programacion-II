import datetime

# Diccionario para almacenar información sobre los vehículos en el parqueadero
parqueadero = {}
# Contadores de vehículos
contadores = {
    "carros": 0,
    "motos": 0,
}
# Tarifa por fracción de hora
tarifa_carro = 2000  # Precio por fracción de carro
tarifa_moto = 1000   # Precio por fracción de moto
# Dinero recogido
dinero_recogido = 0

# Función para registrar la entrada de vehículos
def registrar_entrada(tipo):
    codigo = input("Ingrese el código de 5 dígitos (dejar vacío para generar uno automáticamente): ")
    if not codigo:
        codigo = generar_codigo()
    
    # Verificar si el código ya existe
    if codigo in parqueadero:
        print("El código ya está en uso. Intente nuevamente.")
        return
    
    hora_ingreso = datetime.datetime.now()
    parqueadero[codigo] = {
        "tipo": tipo,
        "hora_ingreso": hora_ingreso
    }
    
    # Incrementar contador
    if tipo == "carro":
        contadores["carros"] += 1
    elif tipo == "moto":
        contadores["motos"] += 1
    
    print(f"Vehículo registrado. Código: {codigo}, Hora de ingreso: {hora_ingreso.strftime('%Y-%m-%d %H:%M:%S')}")

# Función para generar un código aleatorio de 5 dígitos
def generar_codigo():
    import random
    return str(random.randint(10000, 99999))

# Función para calcular el costo del parqueo
def calcular_costo(tipo, tiempo_parqueo):
    fracciones = tiempo_parqueo.total_seconds() // 3600 + (1 if tiempo_parqueo.total_seconds() % 3600 > 0 else 0)
    return fracciones * (tarifa_carro if tipo == "carro" else tarifa_moto)

# Función para registrar la salida de vehículos
def registrar_salida():
    codigo = input("Ingrese el código de 5 dígitos del vehículo: ")
    
    if codigo not in parqueadero:
        print("Código no encontrado. Asegúrese de que el vehículo esté registrado.")
        return
    
    vehiculo = parqueadero[codigo]
    hora_salida = datetime.datetime.now()
    tiempo_parqueo = hora_salida - vehiculo["hora_ingreso"]
    
    costo = calcular_costo(vehiculo["tipo"], tiempo_parqueo)
    global dinero_recogido
    dinero_recogido += costo
    
    print(f"Vehículo tipo {vehiculo['tipo']} registrado. Tiempo de parqueo: {tiempo_parqueo}. Costo: ${costo}.")
    
    # Eliminar vehículo del parqueadero
    del parqueadero[codigo]

# Función para manejar el pago
def manejar_pago(costo):
    print(f"El total a pagar es: ${costo}.")
    while True:
        dinero_recibido = float(input("Ingrese el dinero recibido: $"))
        if dinero_recibido < costo:
            print("El dinero recibido es insuficiente. Intente nuevamente.")
        else:
            vuelto = dinero_recibido - costo
            print(f"Pago exitoso. Su vuelto es: ${vuelto}.")
            break

# Función para mostrar el estado del parqueadero
def mostrar_estado():
    print(f"\n--- Estado del Parqueadero ---")
    print(f"Total de carros ingresados: {contadores['carros']}")
    print(f"Total de motos ingresados: {contadores['motos']}")
    print(f"Dinero recogido: ${dinero_recogido}\n")

# Función principal para el menú
def menu():
    while True:
        print("--- Parqueadero ---")
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar estado del parqueadero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tipo = input("Ingrese el tipo de vehículo (carro/moto): ").lower()
            if tipo in ["carro", "moto"]:
                registrar_entrada(tipo)
            else:
                print("Tipo de vehículo no válido. Intente de nuevo.")
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_estado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
