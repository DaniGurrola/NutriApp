from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/analisis', methods=['GET', 'POST'])
def analisis():
    return render_template('analisis.html', resultado=resultado)

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)
