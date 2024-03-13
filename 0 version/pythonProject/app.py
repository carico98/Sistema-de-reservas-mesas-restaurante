from flask import Flask, render_template, request

app = Flask(__name__)

# Datos del restaurante
restaurante_info = {
    "nombre": "Restaurante La Buena Mesa",
    "direccion": "Calle Principal 123",
    "telefono": "123-456-7890",
    "horario": "9:00 AM - 10:00 PM",
    "dias": "Lunes a Domingo"
}

@app.route('/')
def index():
    return render_template('index.html', restaurante_info=restaurante_info)

@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form['nombre']
    # Aquí puedes procesar la reserva y guardarla en la base de datos
    return 'Reserva realizada con éxito'

if __name__ == '__main__':
    app.run(debug=True)


