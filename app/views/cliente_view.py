from app import app

@app.route('/ola')
def ola():
    return 'olá, mundo em Flask!'