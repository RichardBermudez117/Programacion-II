import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

# Clase para manejar las películas
class Pelicula:
    def __init__(self, nombre, horario, duracion):
        self.nombre = nombre
        self.horario = horario
        self.duracion = duracion
        self.tiquetes_vendidos = 0
        self.dinero_recaudado = 0.0

    def vender_tiquete(self, cantidad):
        precio_tiquete = 50000.0  # Precio fijo de cada tiquete
        self.tiquetes_vendidos += cantidad
        self.dinero_recaudado += cantidad * precio_tiquete

    def obtener_info(self):
        return (f"{self.nombre} - Horario: {self.horario} - Duración: {self.duracion} mins "
                f"- Tiquetes Vendidos: {self.tiquetes_vendidos}")

# Clase para manejar el cine
class Cinema:
    def __init__(self):
        self.peliculas = []
        self.cargar_datos()

    def cargar_datos(self):
        """Cargar las películas desde el archivo CSV"""
        try:
            with open('cartelera.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    nombre, horario, duracion, tiquetes, dinero = row
                    pelicula = Pelicula(nombre, horario, int(duracion))
                    pelicula.tiquetes_vendidos = int(tiquetes)
                    pelicula.dinero_recaudado = float(dinero)
                    self.peliculas.append(pelicula)
        except FileNotFoundError:
            print("Archivo 'cartelera.csv' no encontrado.")

    def guardar_datos(self):
        """Guardar los datos de las películas en el archivo CSV"""
        with open('cartelera.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for pelicula in self.peliculas:
                writer.writerow([pelicula.nombre, pelicula.horario, pelicula.duracion, pelicula.tiquetes_vendidos, pelicula.dinero_recaudado])

    def agregar_pelicula(self, nombre, horario, duracion):
        nueva_pelicula = Pelicula(nombre, horario, duracion)
        self.peliculas.append(nueva_pelicula)
        self.guardar_datos()

    def editar_pelicula(self, nombre, nuevo_horario, nueva_duracion):
        for pelicula in self.peliculas:
            if pelicula.nombre == nombre:
                pelicula.horario = nuevo_horario
                pelicula.duracion = nueva_duracion
                self.guardar_datos()
                return f"Película '{nombre}' ha sido actualizada."

    def eliminar_pelicula(self, nombre):
        self.peliculas = [p for p in self.peliculas if p.nombre != nombre]
        self.guardar_datos()

    def vender_tiquete(self, nombre_pelicula, cantidad):
        for pelicula in self.peliculas:
            if pelicula.nombre == nombre_pelicula:
                pelicula.vender_tiquete(cantidad)
                self.guardar_datos()
                return f"Se vendieron {cantidad} tiquetes para la película '{nombre_pelicula}'."

    def informe(self):
        """Genera un informe para el administrador"""
        total_tiquetes = sum(p.tiquetes_vendidos for p in self.peliculas)
        total_dinero_peliculas = sum(p.dinero_recaudado for p in self.peliculas)

        informe = f"Informe de Administración:\n"
        informe += f"Total de Tiquetes Vendidos: {total_tiquetes}\n"
        informe += f"Dinero Recaudado por Películas: ${total_dinero_peliculas:.2f}\n"
        return informe

# Interfaz gráfica usando tkinter
class InterfazCinema:
    def __init__(self, root, cinema):
        self.root = root
        self.cinema = cinema
        self.root.title("Gestor de Cinema")

        # Menú inicial
        self.menu_inicial()

    def menu_inicial(self):
        """Menú principal para seleccionar si es empleado o cliente"""
        for widget in self.root.winfo_children():
            widget.destroy()  # Limpiar pantalla

        frame = tk.Frame(self.root)
        frame.pack(pady=50)
        label = tk.Label(frame, text="Bienvenido al Cinema", font=("Arial", 16))
        label.pack(pady=10)

        boton_cliente = tk.Button(frame, text="Cliente", command=self.menu_cliente)
        boton_cliente.pack(pady=5)
        boton_empleado = tk.Button(frame, text="Empleado", command=self.menu_empleado)
        boton_empleado.pack(pady=5)

    def menu_cliente(self):
        """Menú para clientes donde pueden ver la cartelera y comprar tiquetes"""
        for widget in self.root.winfo_children():
            widget.destroy()  # Limpiar pantalla

        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        label = tk.Label(frame, text="Cartelera de Películas", font=("Arial", 16))
        label.pack()
        self.mostrar_cartelera(frame)

        entry_pelicula = tk.Entry(frame, width=30)
        entry_pelicula.pack()
        entry_cantidad = tk.Entry(frame, width=10)
        entry_cantidad.pack()
        boton_comprar = tk.Button(frame, text="Comprar Tiquetes", command=lambda: self.vender_tiquetes(entry_pelicula.get(), entry_cantidad.get()))
        boton_comprar.pack()

        boton_volver = tk.Button(frame, text="Volver", command=self.menu_inicial)
        boton_volver.pack()

    def menu_empleado(self):
        """Menú para empleados donde pueden gestionar las películas y generar informes"""
        for widget in self.root.winfo_children():
            widget.destroy()  # Limpiar pantalla

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        label = tk.Label(frame, text="Gestión de Empleados", font=("Arial", 16))
        label.pack()

        boton_agregar = tk.Button(frame, text="Agregar Película", command=self.agregar_pelicula)
        boton_agregar.pack(pady=5)
        boton_editar = tk.Button(frame, text="Editar Película", command=self.editar_pelicula)
        boton_editar.pack(pady=5)
        boton_eliminar = tk.Button(frame, text="Eliminar Película", command=self.eliminar_pelicula)
        boton_eliminar.pack(pady=5)
        boton_informe = tk.Button(frame, text="Generar Informe", command=self.generar_informe)
        boton_informe.pack(pady=5)
        boton_volver = tk.Button(frame, text="Volver", command=self.menu_inicial)
        boton_volver.pack(pady=5)

    def mostrar_cartelera(self, frame):
        """Muestra la cartelera de películas"""
        cartelera = "\n".join([p.obtener_info() for p in self.cinema.peliculas])
        label_cartelera = tk.Label(frame, text=cartelera, font=("Arial", 12), justify=tk.LEFT)
        label_cartelera.pack()

    def vender_tiquetes(self, nombre_pelicula, cantidad):
        try:
            cantidad = int(cantidad)
            mensaje = self.cinema.vender_tiquete(nombre_pelicula, cantidad)
            messagebox.showinfo("Venta de Tiquetes", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido de tiquetes")

    def agregar_pelicula(self):
        nombre = simpledialog.askstring("Agregar Película", "Nombre de la película:")
        horario = simpledialog.askstring("Agregar Película", "Horario de la película:")
        duracion = simpledialog.askinteger("Agregar Película", "Duración (en minutos):")
        if nombre and horario and duracion:
            self.cinema.agregar_pelicula(nombre, horario, duracion)
            messagebox.showinfo("Agregar Película", f"Película '{nombre}' agregada correctamente")

    def editar_pelicula(self):
        nombre = simpledialog.askstring("Editar Película", "Nombre de la película a editar:")
        if nombre:
            nuevo_horario = simpledialog.askstring("Editar Película", "Nuevo horario:")
            nueva_duracion = simpledialog.askinteger("Editar Película", "Nueva duración (en minutos):")
            if nuevo_horario and nueva_duracion:
                mensaje = self.cinema.editar_pelicula(nombre, nuevo_horario, nueva_duracion)
                messagebox.showinfo("Editar Película", mensaje)

    def eliminar_pelicula(self):
        nombre = simpledialog.askstring("Eliminar Película", "Nombre de la película a eliminar:")
        if nombre:
            self.cinema.eliminar_pelicula(nombre)
            messagebox.showinfo("Eliminar Película", f"Película '{nombre}' eliminada correctamente")

    def generar_informe(self):
        informe = self.cinema.informe()
        messagebox.showinfo("Informe", informe)

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    cinema = Cinema()
    interfaz = InterfazCinema(root, cinema)
    root.mainloop()
