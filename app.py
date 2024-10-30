from flask import Flask, render_template, request, redirect, url_for
from cedula import CedulaChecker
#import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Obtener el valor del input por su nombre en el formulario (request.form es un diccionario de valores)
    valor = request.form.get('cedula-value')

    checker = CedulaChecker(valor)
    checker.validate()
    
    # Imprimir el valor en la consola
    # print(f"Valor recibido: {}")
    # # if request.method == 'POST':
        # Captura los datos del formulario
        # name = request.form['name']
        # email = request.form['email']
        
        # Guarda los datos en la base de datos
        # with sqlite3.connect(DATABASE) as conn:
        #     cursor = conn.cursor()
        #     cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        #     conn.commit()
        
        # return redirect(url_for('index'))
    
    # Muestra el formulario
    return render_template('index.html')

if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
