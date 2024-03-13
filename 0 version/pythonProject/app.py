from flask import Flask, render_template, request
import psycopg2

app = Flask(_name_)

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="reserva_restaurantes",
    user="postgres",
    password="1998Arico",
    host="127.0.0.1",
    port="5432",
    client_encoding="utf-8"
)

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
    # Extraer datos del formulario de reserva
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    telefono = request.form['telefono']
    fecha = request.form['fecha']
    hora = request.form['hora']

    # Insertar datos en la base de datos
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservaciones (nombre, apellido, cedula, telefono, fecha, hora)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, apellido, cedula, telefono, fecha, hora))
    conn.commit()
    cursor.close()

    # Devolver mensaje de confirmación
    return 'Reserva realizada con éxito'

@app.route('/verificar_reserva', methods=['POST'])
def verificar_reserva():
    # Obtener la cédula del formulario
    cedula = request.form['cedula']

    # Verificar si la cédula está en la base de datos
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservaciones WHERE cedula = %s", (cedula,))
    reserva = cursor.fetchone()
    cursor.close()

    if reserva:
        mensaje = "Usted tiene una reservación"
    else:
        mensaje = "Usted no tiene una reservación"

    return mensaje

if _name_ == '_main_':
    app.run(debug=True)
