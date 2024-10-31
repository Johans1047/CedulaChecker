from flask import Flask, render_template, request, url_for
from cedula import CedulaChecker
from errors import InvalidFormat

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Obtener el valor del input por su nombre en el formulario (request.form es un diccionario de valores) en el metodo POST
    if request.method == 'POST':
        cedula = request.form.get('cedula-value')
        checker = CedulaChecker(cedula)
        
        try:
            ced_type, province = checker.validate()
        except InvalidFormat as e:
            print(e)
            return render_template('index.html', alerta='error')
        
        formatted_cedula, prefix, book, volume = checker.format()
        
        resultado = {
            'patron': cedula,
            'cedula': formatted_cedula,
            'tipo': ced_type,
            'provincia': province,
            'longitud': len(formatted_cedula),
            'prefijo': prefix,
            'libro': book,
            'tomo': volume
        }
            
        return render_template('index.html', resultado=resultado, alerta='exito')
    
    # Muestra el formulario
    return render_template('index.html')

if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
