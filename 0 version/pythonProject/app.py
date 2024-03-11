import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Reservas de Mesas")

        self.nombre_label = tk.Label(master, text="Nombre del Cliente:")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        self.apellido_label = tk.Label(master, text="Apellido del Cliente:")
        self.apellido_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.apellido_entry = tk.Entry(master)
        self.apellido_entry.grid(row=1, column=1, padx=10, pady=5)

        self.cedula_label = tk.Label(master, text="Cédula del Cliente:")
        self.cedula_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.cedula_entry = tk.Entry(master)
        self.cedula_entry.grid(row=2, column=1, padx=10, pady=5)

        self.telefono_label = tk.Label(master, text="Número Telefónico:")
        self.telefono_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.telefono_entry = tk.Entry(master)
        self.telefono_entry.grid(row=3, column=1, padx=10, pady=5)

        self.hora_label = tk.Label(master, text="Hora de la Reserva:")
        self.hora_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.hora_entry = tk.Entry(master)
        self.hora_entry.grid(row=4, column=1, padx=10, pady=5)

        self.confirmar_button = tk.Button(master, text="Confirmar Reserva", command=self.confirmar_reserva)
        self.confirmar_button.grid(row=5, column=0, pady=10)

        self.rechazar_button = tk.Button(master, text="Rechazar Reserva", command=self.rechazar_reserva)
        self.rechazar_button.grid(row=5, column=1, pady=10)

    def confirmar_reserva(self):
        nombre_cliente = self.nombre_entry.get()
        apellido_cliente = self.apellido_entry.get()
        cedula_cliente = self.cedula_entry.get()
        telefono_cliente = self.telefono_entry.get()
        hora_reserva = self.hora_entry.get()

        if nombre_cliente and apellido_cliente and cedula_cliente and telefono_cliente and hora_reserva:
            messagebox.showinfo("Reserva Confirmada", f"Reserva confirmada para {nombre_cliente} {apellido_cliente}. Hora: {hora_reserva}")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def rechazar_reserva(self):
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.cedula_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
