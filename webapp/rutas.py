from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola World'

@app.route('/tutoriales')
def tutoriales():
    return 'Aqui encontraras los mis tutoriales'

@app.route('/cursos')
def cursos():
    return 'Aqui cursos'
 

if __name__ =='__main__':
    app.run(debug=True, host = '0.0.0.0')

