from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    edad = None
    cantidad_taros = None
    total_sin_descuento = None
    descuento_en_dinero = None
    total_a_pagar = None

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        edad = request.form.get('edad', '').strip()
        cantidad_taros = request.form.get('cantidad_taros', '').strip()

        edad = int(edad)
        cantidad_taros = int(cantidad_taros)

        total_sin_descuento = cantidad_taros * 9000

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_en_dinero = total_sin_descuento * descuento

        total_a_pagar = total_sin_descuento - descuento_en_dinero

    return render_template('ejercicio1.html', nombre=nombre, edad=edad, cantidad_taros=cantidad_taros,
                           total_sin_descuento=total_sin_descuento, descuento_en_dinero=descuento_en_dinero,
                           total_a_pagar=total_a_pagar)

usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    nombre1 = None
    nombre2 = None

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')

        if not nombre1 or not nombre2:
            mensaje = "Por favor, ingrese tanto el nombre de usuario como la contraseña."
            return render_template('ejercicio2.html', mensaje=mensaje, nombre1=nombre1, nombre2=nombre2)

        if nombre1 in usuarios and usuarios[nombre1] == nombre2:
            if nombre1 == 'juan':
                mensaje = f"Bienvenido Administrador {nombre1}"
            elif nombre1 == 'pepe':
                mensaje = f"Bienvenido Usuario {nombre1}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje, nombre1=nombre1, nombre2=nombre2)

if __name__ == '__main__':
    app.run()