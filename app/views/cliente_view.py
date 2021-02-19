from app import app

@app.route('/ola', defaults={'nome': None}, methods={"POST", "GET"})
@app.route('/ola/<string:nome>')
def ola(nome):
    if nome:
        return f'olá, {nome}'
    else:
        return f'Olá, usuario'

@app.route('/')
def home():
    return "Hello World"