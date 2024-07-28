# criando formulários de login e criar conta para o site
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao = SubmitField('Confirmar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário não encontrado. Crie uma conta")


class FormCriarConta(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,16)])
    confirmar_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo("senha")])
    botao = SubmitField('Enviar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Este e-mail já está cadastrado, faça login")


class FormFoto(FlaskForm):
    foto = FileField('Foto', validators={DataRequired()})
    confirmar = SubmitField('Enviar')