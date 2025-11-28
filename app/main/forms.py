from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    disciplinas = SelectField(
        'Disciplina',
        choices=[
            ('DSWA5', 'DSWA5'),
            ('GPSA5', 'GPSA5'),
            ('IHCA5', 'IHCA5'),
            ('SODA5', 'SODA5'),
            ('PJIA5', 'PJIA5'),
            ('TCOA5', 'TCOA5'),
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField('Enviar')
