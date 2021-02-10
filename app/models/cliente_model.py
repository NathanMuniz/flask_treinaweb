from app import db
from sqlalchemy_utils import ChoiceType

class Cliente(db.Model):
    __tablename__ = 'clientes'

    SEXO_CHOICES = [
        (u'm', u'Masculino'),
        (u'f', u'Feminino'),
        (u'N', u'Nenhuma das opções')
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nacimento = db.Column(db.DateTime)
    profissao = db.Column(db.String(30))
    sexo = db.Column(ChoiceType(SEXO_CHOICES))