from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# CONFIGURANDO A CRIAÇÃO DO BANCO DE DADOS
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
database = SQLAlchemy(app)

app.config["SECRET_KEY"] = "074fe331335d77ac3e70c298572ff506" # CHAVE SECRETA HASH PARA LOGIN
app.config['UPLOAD_FOLDER'] = 'static/fotos_post' # SALVAR O ARQUIVO DENTRO DA PASTA fotos_post
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from Fakepinterest import route