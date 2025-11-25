from flask import render_template
from . import main
from ..models import User, Cadastro
from .forms import CadastroForm
from .. import db
from app import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = CadastroForm()

    if form.validate_on_submit():
        cadastro = Cadastro(
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            instituicao=form.instituicao.data,
            disciplinas=",".join(form.disciplinas.data)
        )
        db.session.add(cadastro)
        db.session.commit()

        return redirect(url_for('main.formulario'))

    cadastros = Cadastro.query.all()
    return render_template('formulario.html', form=form, cadastros=cadastros)

@main.route('/usuarios')
def usuarios():
    users = User.query.all()
    return render_template('usuarios.html', users=users)

