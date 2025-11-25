from flask import render_template
from . import main
from ..models import User

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = CadastroForm()
    resultados = None

    if form.validate_on_submit():
        resultados = {
            'nome': form.nome.data,
            'sobrenome': form.sobrenome.data,
            'instituicao': form.instituicao.data,
            'disciplinas': form.disciplinas.data,
        }

    return render_template('formulario.html', form=form, resultados=resultados)


@main.route('/usuarios')
def usuarios():
    users = User.query.all()
    return render_template('usuarios.html', users=users)

