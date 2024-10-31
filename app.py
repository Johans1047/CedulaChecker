from flask import Flask, Response, render_template, request, url_for
from cedula import CedulaChecker
from api import CedulaCheckerAPI
from errors import InvalidFormat
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles GET and POST requests for the main page.
    
    POST:
        Validates and formats the entered cedula, then renders the result.
    
    GET:
        Renders the main form page.
    
    Returns
    -------
    str
        Rendered HTML page with results if POST, or just the form if GET.
    """
    
    if request.method == 'POST':
        cedula = request.form.get('cedula-value')
        checker = CedulaChecker(cedula)
        
        try:
            ced_type, province = checker.validate()
        except InvalidFormat as e:
            print(e)
            return render_template('index.html', alert='error')
        
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
            
        return render_template('index.html', resultado=resultado, alert='success')
    
    return render_template('index.html')

@app.route('/api/cedula')
def get_cedula_formatted():
    result = CedulaCheckerAPI("3-747-2358").check()
    response = Response(json.dumps(result), mimetype='application/json')
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)