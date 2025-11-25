from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    instituicao = StringField('Instituição', validators=[DataRequired()])

    disciplinas = SelectMultipleField(
        'Disciplinas',
        choices=[
            ('matematica', 'Matemática'),
            ('fisica', 'Física'),
            ('quimica', 'Química'),
            ('biologia', 'Biologia'),
            ('portugues', 'Português'),
            ('historia', 'História'),
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField('Enviar')