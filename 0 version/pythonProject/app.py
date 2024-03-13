from flask import Flask, render_template, request

app = Flask(__name__)

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = {}

    def agregar_mesa(self, mesa):
        self.mesas[mesa.numero] = mesa

    def hacer_reserva(self, nombre_cliente, numero_personas, mesa_numero, fecha_hora):
        if mesa_numero in self.mesas:
            mesa = self.mesas[mesa_numero]
            reserva = Reserva(nombre_cliente, numero_personas, fecha_hora)
            if mesa.reservar(reserva):
                return f"Reserva realizada para {nombre_cliente} en la mesa {mesa_numero} el {fecha_hora}."
            else:
                return f"Lo sentimos, la mesa {mesa_numero} no está disponible para {numero_personas} personas en ese momento."
        else:
            return f"No existe la mesa {mesa_numero} en {self.nombre}."


class Mesa:
    def __init__(self, numero, capacidad, disponible=True):
        self.numero = numero
        self.capacidad = capacidad
        self.disponible = disponible
        self.reserva = None

    def reservar(self, reserva):
        if self.disponible and self.capacidad >= reserva.numero_personas:
            self.disponible = False
            self.reserva = reserva
            return True
        else:
            return False


class Reserva:
    def __init__(self, nombre_cliente, numero_personas, fecha_hora):
        self.nombre_cliente = nombre_cliente
        self.numero_personas = numero_personas
        self.fecha_hora = fecha_hora


restaurante = Restaurante("Mi Restaurante")
restaurante.agregar_mesa(Mesa(1, 4))
restaurante.agregar_mesa(Mesa(2, 6))
restaurante.agregar_mesa(Mesa(3, 2))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        numero_personas = int(request.form['numero_personas'])
        mesa_numero = int(request.form['mesa_numero'])
        fecha_hora = request.form['fecha_hora']

        mensaje = restaurante.hacer_reserva(nombre_cliente, numero_personas, mesa_numero, fecha_hora)
        return render_template('index.html', mensaje=mensaje)
    else:
        return render_template('index.html', mensaje='')


if __name__ == '__main__':
    app.run(debug=True)


