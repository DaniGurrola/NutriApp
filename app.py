from flask import Flask, render_template, request, redirect
import pymysql


app = Flask(__name__)
app.secret_key = "mi_clave_secreta" 

def get_connection():
    return pymysql.connect(
        host='localhost',     
        user='root',       
        password='',         
        db='usuariosdb',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['nombre']
            return redirect('/') 
        else:
            return "Correo o contraseña incorrectos"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()  
    return redirect('/')




@app.route('/recetas')
def recetas():
    recetas_disponibles = [
        {
            'nombre': 'Ensalada de Quinoa y Aguacate',
            'calorias': 350,
            'ingredientes': ['Quinoa', 'Aguacate', 'Tomate cherry', 'Pepino', 'Limón', 'Aceite de Oliva'],
            'preparacion': 'Cocinar la quinoa siguiendo las instrucciones del paquete. Picar el aguacate, tomate y pepino. Mezclar todos los ingredientes y aderezar con una vinagreta simple de limón, aceite de oliva y sal.'
        },
        {
            'nombre': 'Salmón al Horno con Espárragos',
            'calorias': 480,
            'ingredientes': ['Filete de Salmón (150g)', 'Espárragos (1 manojo)', 'Aceite de oliva', 'Ajo en polvo', 'Pimienta'],
            'preparacion': 'Precalentar el horno a 200°C. Sazonar el salmón con ajo, sal y pimienta. Rociar los espárragos con aceite. Hornear todo junto durante 12-15 minutos, hasta que el salmón esté cocido.'
        },
        {
            'nombre': 'Tazón de Avena Nocturna (Overnight Oats)',
            'calorias': 290,
            'ingredientes': ['Avena en hojuelas', 'Leche (o bebida vegetal)', 'Semillas de Chía', 'Miel o Stevia', 'Fruta fresca'],
            'preparacion': 'Mezclar la avena, leche, chía y edulcorante en un frasco. Refrigerar durante toda la noche. Por la mañana, añadir la fruta fresca y disfrutar.'
        }
    ]
    
    return render_template('recetas.html', recetas=recetas_disponibles)


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

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']

            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, email, password))
            conn.commit()

            print("GUARDADO OK") 

            return redirect('/') 

        except Exception as e:
            print("ERROR:", e) 
            return "Error: " + redirect('/')

    return render_template('registro.html')



if __name__ == "__main__":
    app.run(debug=True)
