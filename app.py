from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return ('''
<h1> Bienvenido a la calculadora desde Flask </h1>
    <p> Para teclear en las sumas pon en el navegador (o haz clic aquí): 
        <a href="/sumar/89/5">http://127.0.0.1:5000/sumar/89/5</a>
    </p>
    <p> Para teclear en las restas pon en el navegador (o haz clic aquí): 
        <a href="/resta/10/5">http://127.0.0.1:5000/resta/10/5</a> 
    </p>
    <p> Para teclear en las multiplicaciones pon en el navegador (o haz clic aquí): 
        <a href="/multiplicar/10/5">http://127.0.0.1:5000/multiplicar/10/5</a> 
    </p>
    <p> Para teclear en las divisiones pon en el navegador (o haz clic aquí): 
        <a href="/dividir/10/5">http://127.0.0.1:5000/dividir/10/5</a> 
    </p>
    <p> Para teclear en las menores pon en el navegador (o haz clic aquí): 
        <a href="/menor/10/5">http://127.0.0.1:5000/menor/10/5</a> 
    </p>
    <p> Para teclear en las mayores pon en el navegador (o haz clic aquí): 
        <a href="/mayor/10/5">http://127.0.0.1:5000/mayor/10/5</a> 
    </p>
<footer> De La Cruz Sergio René. 5.D </footer>
''')

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a , b):
    return str(a + b)

@app.route('/resta/<int:a>/<int:b>')
def resta(a, b):
    return str(a - b)

@app.route('/multiplicar/<int:a>/<int:b>')
def multiplicar(a, b):
    return str(a * b)

@app.route('/dividir/<int:a>/<int:b>')
def dividir(a, b):
    return str(a / b)

@app.route('/menor/<int:a>/<int:b>')
def menor(a, b):
    return str(min(a, b))

@app.route('/mayor/<int:a>/<int:b>')
def mayor(a , b):
    return str(max(a, b))

if __name__ == '__main__':
    app.run(debug=True)
