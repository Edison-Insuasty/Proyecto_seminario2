from flask import Flask, render_template
from flask import Flask 
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template

from flask import make_response
from flask import jsonify
from datetime import timedelta
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/productos')
def mostrarProductos():
    misProductos = ("POLLO BROASTER:  El pollo estilo broaster, es un pollo frito muy sabroso y crujiente que últimamente se viene sirviendo en muchos restaurantes de comida rápida (Tipo KFC) e incluso algunas versiones gourmet en restaurantes importantes. La mayoría de estos, se especializan en preparar este estilo de pollo rebozado con sabores tradicionales.", 
                    "HAMBURGUESA:   ", 
                    "PAPA MIXTA", 
                    "PERRO CALIENTE",
                    "PIZZA", 
                    "SANDWICH CUBANO", 
                    "CARNE", 
                    "FILETE DE POLLO",
                    "PAPA RELLENA", )

    return render_template('productos.html', productos=misProductos)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)
