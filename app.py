from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '''
<h1>¡Hola mundo desde Flask!</h1>
<p> Texto random 1 </p>
<p> Texto random 2 </p>
<p> Texto random 3 </p>
<p> Texto random 4 </p>
<p> Texto random 5 </p>
'''
@app.route('/factorial/<v1>')
def factorial(v1):
    fact=1
    for x in range(1, int(v1) +1):
        fact*=x
    return (f"El factorial de {v1}! es {fact}")

@app.route('/otra')
def hola_mundo1():
    return '<h1> ¡Hola mundo desde otra ruta!</h1>'
if __name__ == '__main__':
    app.run(debug=True)
    