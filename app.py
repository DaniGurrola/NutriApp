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

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    resultados = {}
    
    if request.method == 'POST':
        food_name = request.form['foodName']
        weight_grams = float(request.form['weightGrams'])
        cals_per_100 = float(request.form['calsPer100'])
        protein_per_100 = float(request.form['proteinPer100'])
        carbs_per_100 = float(request.form['carbsPer100'])
        fat_per_100 = float(request.form['fatPer100'])
        
        factor = weight_grams / 100

        resultados['outputFoodName'] = food_name
        resultados['outputWeight'] = f'{round(weight_grams)} g'
        resultados['outputCalories'] = round_one_decimal(cals_per_100 * factor)
        resultados['outputProtein'] = round_one_decimal(protein_per_100 * factor)
        resultados['outputCarbs'] = round_one_decimal(carbs_per_100 * factor)
        resultados['outputFat'] = round_one_decimal(fat_per_100 * factor)


    return render_template('calculadora.html', resultados=resultados)

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)
