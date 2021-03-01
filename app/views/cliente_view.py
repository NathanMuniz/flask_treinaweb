from flask import render_template

from app import app

@app.route('/ola', defaults={'nome': None}, methods={"POST", "GET"})
@app.route('/ola/<string:nome>')
def ola(nome):
    return render_template("clientes/teste.html", nome_usuario=nome)

@app.route('/')
def home():
    return "Hello World"