from flask import render_template
from . import main
from ..models import User
from .forms import CadastroForm
from .. import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = CadastroForm()

    if form.validate_on_submit():

        disciplinas_str = ", ".join(form.disciplinas.data)

        cadastro = Cadastro(
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            instituicao=form.instituicao.data,
            disciplinas=disciplinas_str
        )

        db.session.add(cadastro)
        db.session.commit()

        return redirect(url_for('main.usuarios'))

    return render_template('formulario.html', form=form)

@main.route('/usuarios')
def usuarios():
    users = User.query.all()
    return render_template('usuarios.html', users=users)

