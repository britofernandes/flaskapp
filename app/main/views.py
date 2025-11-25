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
    resultados = None

    if form.validate_on_submit():

        # transformar lista em string para salvar
        disciplinas_str = ",".join(form.disciplinas.data)

        cadastro = Cadastro(
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            instituicao=form.instituicao.data,
            disciplinas=disciplinas_str
        )

        db.session.add(cadastro)
        db.session.commit()

        resultados = {
            'nome': cadastro.nome,
            'sobrenome': cadastro.sobrenome,
            'instituicao': cadastro.instituicao,
            'disciplinas': cadastro.disciplinas.split(','),
        }

    return render_template('formulario.html', form=form, resultados=resultados)


@main.route('/usuarios')
def usuarios():
    users = User.query.all()
    return render_template('usuarios.html', users=users)

