from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    instituicao = StringField('Instituição', validators=[DataRequired()])

   disciplinas = SelectField('Disciplina', choices=[
    ('matematica', 'Matemática'),
    ('portugues', 'Português'),
    ('historia', 'História'),
    ('geografia', 'Geografia'),
],
        validators=[DataRequired()]
    )

    submit = SubmitField('Enviar')