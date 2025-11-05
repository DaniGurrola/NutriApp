from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciosesion')
def iniciosesion():
    return render_template('iniciosesion.html')

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/analisis', methods=['GET', 'POST'])
def analisis():
    resultado = None

    if request.method == 'POST':
        comida = request.form['comida']
        calorias = int(request.form['calorias'])
        grasas = int(request.form['grasas'])
        azucar = int(request.form['azucar'])

        if calorias < 300 and grasas < 10 and azucar < 5:
            resultado = f"La comida '{comida}' es saludable."
        else:
            resultado = f"La comida '{comida}' no es saludable."

    return render_template('analisis.html', resultado=resultado)

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)
