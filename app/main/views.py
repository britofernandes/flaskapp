from flask import render_template, redirect, url_for
from . import main
from ..models import User, Cadastro
from .forms import CadastroForm
from .. import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = CadastroForm()

    if form.validate_on_submit():
        cadastro = Cadastro(
            nome=form.nome.data,
            disciplinas=form.disciplinas.data
        )
        db.session.add(cadastro)
        db.session.commit()

        return redirect(url_for('main.professores'))

    cadastros = Cadastro.query.all()
    return render_template('professores.html', form=form, cadastros=cadastros)


@main.route('/usuarios')
def usuarios():
    users = User.query.all()
    return render_template('usuarios.html', users=users)

