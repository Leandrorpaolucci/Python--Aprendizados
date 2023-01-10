from flask_wtf import FlaskForm  #      |     FlaskForm recebeu por herança as funcionalidades de criação do forms
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField  #    | Tipos de campos no formulários
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sitecomunidade.models import Usuario
from flask_login import current_user

"""'Validators'
------------------------------------------------------------
DataRequired = Campo Obrigatório
Length = Estabelecer o minimo de caractere para senha
Email = Verificar se é realmente um e-mail válido
EqualTo = Verificar se a senha é igual
------------------------------------------------------------
Qualquer método acima tem que ser iniciado como lista, independente que seja só um deles.
confirmar_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(),  EqualTo('senha')])
EqualTo('senha')] = se fosse para qualquer outro campo a confirmação do mesmo nome é dessa maneira
"""


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(),  EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail ja cadastrado. Cadastre-se com outro e-mail')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    curso_excel = BooleanField('Curso Excel')
    curso_sql = BooleanField('Curso SQL')
    curso_python = BooleanField('Curso Python')

    def validate_email(self, email):
        #verificar se o usuario mudou de email para evitar conflito com outros usuarios se porventura existir um email ja existente
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre um novo e-mail', 'alert-danger')


