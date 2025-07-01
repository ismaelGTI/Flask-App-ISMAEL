
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para mensajes flash


# Página sorpresa creativa
@app.route('/sorpresa')
def sorpresa():
    return render_template('sorpresa.html')

@app.route('/')
def home():
    return render_template('index.html')

# Página sobre mí

# Página sobre mí
@app.route('/about')
def about():
    return render_template('about.html')




# Ruta para mostrar y procesar el formulario de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        if not nombre or not email or not mensaje:
            flash('Por favor, completa todos los campos.', 'error')
            return redirect(url_for('contacto'))
        # Guardar mensaje en un archivo
        with open('mensajes.txt', 'a', encoding='utf-8') as f:
            f.write(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}\n---\n")
        flash('¡Mensaje enviado correctamente!', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
