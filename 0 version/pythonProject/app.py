import tkinter as tk
from tkinter import ttk, messagebox

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurante La Buena Mesa")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        # Pestaña "Conoce un poco más de nosotros"
        self.tab_conocenos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_conocenos, text="Conoce un poco más de nosotros")
        self.descripcion_label = tk.Label(self.tab_conocenos, text="Descripción: Restaurante La Buena Mesa ofrece una amplia variedad de platos...")
        self.descripcion_label.pack(padx=10, pady=10)

        # Pestaña "Reservas"
        self.tab_reservas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reservas, text="Reservas")

        self.nombre_label = tk.Label(self.tab_reservas, text="Nombre del Cliente:")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nombre_entry = tk.Entry(self.tab_reservas)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        # Agrega más campos y botones según tus necesidades

        self.confirmar_button = tk.Button(self.tab_reservas, text="Confirmar Reserva", command=self.confirmar_reserva)
        self.confirmar_button.grid(row=5, column=0, pady=10)

        self.rechazar_button = tk.Button(self.tab_reservas, text="Rechazar Reserva", command=self.rechazar_reserva)
        self.rechazar_button.grid(row=5, column=1, pady=10)

        # Pestaña "Menú"
        self.tab_menu = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_menu, text="Menú")
        self.menu_label = tk.Label(self.tab_menu, text="Aquí estará nuestro menú con una amplia variedad de platos...")
        self.menu_label.pack(padx=10, pady=10)

    def confirmar_reserva(self):
        nombre_cliente = self.nombre_entry.get()
        # Implementa la función de confirmar reserva
        if nombre_cliente:
            messagebox.showinfo("Reserva Confirmada", f"Reserva confirmada para {nombre_cliente}.")
        else:
            messagebox.showerror("Error", "Debe ingresar el nombre del cliente antes de confirmar la reserva.")

    def rechazar_reserva(self):
        # Implementa la función de rechazar reserva
        nombre_cliente = self.nombre_entry.get()
        if nombre_cliente:
            messagebox.showinfo("Reserva Rechazada", f"La reserva para {nombre_cliente} ha sido rechazada.")
        else:
            messagebox.showerror("Error", "Debe ingresar el nombre del cliente antes de rechazar la reserva.")

def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

