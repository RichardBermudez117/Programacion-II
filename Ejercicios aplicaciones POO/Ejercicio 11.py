import csv
import os

class Usuario:
    def __init__(self, nombre, contraseña, tipo):
        self.nombre = nombre
        self.contraseña = contraseña
        self.tipo = tipo  # 'frecuente' o 'visitante'

class Empleado(Usuario):
    def __init__(self, nombre, contraseña):
        super().__init__(nombre, contraseña, 'empleado')

class Pelicula:
    def __init__(self, nombre, horarios):
        self.nombre = nombre
        self.horarios = horarios  # Lista de horarios disponibles
        self.tickets_vendidos = {horario: 0 for horario in horarios}  # Inicializa tickets vendidos por horario

    def vender_ticket(self, horario):
        if self.tickets_vendidos[horario] < 10:  # Capacidad de la sala
            self.tickets_vendidos[horario] += 1
            return True
        return False

class Comida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cinema:
    def __init__(self):
        self.peliculas = []
        self.comidas = []
        self.tickets_vendidos = []
        self.ventas_comida = []

    def agregar_pelicula(self, nombre, horarios):
        nueva_pelicula = Pelicula(nombre, horarios)
        self.peliculas.append(nueva_pelicula)

    def mostrar_cartelera(self):
        print("Cartelera de películas:")
        for pelicula in self.peliculas:
            print(f" - {pelicula.nombre} | Horarios: {', '.join(pelicula.horarios)}")

    def comprar_ticket(self, pelicula_nombre, horario, usuario):
        for pelicula in self.peliculas:
            if pelicula.nombre == pelicula_nombre:
                if pelicula.vender_ticket(horario):
                    self.tickets_vendidos.append({
                        'pelicula': pelicula_nombre,
                        'horario': horario,
                        'usuario': usuario.nombre
                    })
                    print(f"Ticket vendido para {pelicula_nombre} a las {horario}.")
                    return True
                else:
                    print("No hay disponibilidad para esta función.")
                    return False
        print("Película no encontrada.")
        return False

    def agregar_comida(self, nombre, precio):
        nueva_comida = Comida(nombre, precio)
        self.comidas.append(nueva_comida)

    def mostrar_comidas(self):
        print("Menú de comidas:")
        for comida in self.comidas:
            print(f" - {comida.nombre}: ${comida.precio}")

    def vender_comida(self, nombre, cantidad):
        for comida in self.comidas:
            if comida.nombre == nombre:
                total = comida.precio * cantidad
                self.ventas_comida.append({'comida': comida.nombre, 'cantidad': cantidad, 'total': total})
                print(f"Se vendieron {cantidad} de {comida.nombre} por un total de ${total}.")
                return total
        print("Comida no encontrada.")
        return 0

    def generar_informe(self):
        with open('informe_cinema.csv', 'w', newline='') as csvfile:
            fieldnames = ['pelicula', 'horario', 'usuario']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ticket in self.tickets_vendidos:
                writer.writerow(ticket)

        print("Informe generado en 'informe_cinema.csv'.")

def menu_principal():
    cinema = Cinema()
    # Agregar algunas películas y comidas de ejemplo
    cinema.agregar_pelicula("Avengers: Endgame", ["11:30", "14:00", "16:30", "19:00"])
    cinema.agregar_pelicula("Inception", ["11:30", "14:00", "16:30", "19:00"])
    cinema.agregar_comida("Popcorn", 5)
    cinema.agregar_comida("Soda", 3)

    usuarios = {
        "empleado1": Empleado("empleado1", "pass123"),
        "frecuente1": Usuario("frecuente1", "pass123", "frecuente"),
        "visitante1": Usuario("visitante1", "pass123", "visitante")
    }

    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar como empleado")
        print("2. Ingresar como usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            empleado = usuarios.get(nombre)
            if isinstance(empleado, Empleado) and empleado.contraseña == contraseña:
                print(f"Bienvenido {empleado.nombre}!")
                while True:
                    print("\n--- Menú Empleado ---")
                    print("1. Mostrar cartelera")
                    print("2. Generar informe")
                    print("3. Salir")
                    opcion_empleado = input("Seleccione una opción: ")

                    if opcion_empleado == "1":
                        cinema.mostrar_cartelera()
                    elif opcion_empleado == "2":
                        cinema.generar_informe()
                    elif opcion_empleado == "3":
                        break
                    else:
                        print("Opción no válida.")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "2":
            tipo_usuario = input("Seleccione tipo de usuario (frecuente/visitante): ").strip().lower()
            if tipo_usuario == "frecuente":
                nombre = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")
                usuario = usuarios.get(nombre)
                if isinstance(usuario, Usuario) and usuario.contraseña == contraseña and usuario.tipo == "frecuente":
                    print(f"Bienvenido {usuario.nombre}!")
                    while True:
                        print("\n--- Menú Usuario Frecuente ---")
                        print("1. Mostrar cartelera")
                        print("2. Comprar ticket")
                        print("3. Reservar película")
                        print("4. Salir")
                        opcion_usuario = input("Seleccione una opción: ")

                        if opcion_usuario == "1":
                            cinema.mostrar_cartelera()
                        elif opcion_usuario == "2":
                            pelicula = input("Ingrese el nombre de la película: ")
                            horario = input("Ingrese el horario: ")
                            cinema.comprar_ticket(pelicula, horario, usuario)
                        elif opcion_usuario == "3":
                            print("Funcionalidad de reserva no implementada.")
                        elif opcion_usuario == "4":
                            break
                        else:
                            print("Opción no válida.")
                else:
                    print("Usuario o contraseña incorrectos.")
            elif tipo_usuario == "visitante":
                print("Bienvenido visitante!")
                while True:
                    print("\n--- Menú Usuario Visitante ---")
                    print("1. Mostrar cartelera")
                    print("2. Comprar ticket")
                    print("3. Salir")
                    opcion_visitante = input("Seleccione una opción: ")

                    if opcion_visitante == "1":
                        cinema.mostrar_cartelera()
                    elif opcion_visitante == "2":
                        pelicula = input("Ingrese el nombre de la película: ")
                        horario = input("Ingrese el horario: ")
                        cinema.comprar_ticket(pelicula, horario, None)
                    elif opcion_visitante == "3":
                        break
                    else:
                        print("Opción no válida.")
            else:
                print("Tipo de usuario no válido.")

        elif opcion == "3":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida.")
            menu_principal()

if __name__ == "__main__":
    menu_principal()
