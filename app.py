# execução normal
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

# execução com Python/Flash dentro do docker
# docker run -t -i -p 5000:5000   <Nome da imagem>
# Caso queira que o docker acesse o projeto no micro local adicionar 
#-v <diretório local do projeto>:<Diretorio dentro do docker>

from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
from models import Posto
from dao import PostoDao
import os, datetime
#import sqlite3
from werkzeug.exceptions import abort

#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "sqlite:///{}".format(os.path.join(project_dir, 'database.db'))

app = Flask(__name__)
app.secret_key = 'app'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "pi_grupo04_2021"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

posto_dao = PostoDao(db)


@app.route('/')
def index():
    return render_template('index.html', titulo='Buscador de preços de combustíveis')


@app.route('/create')
def novoPosto():
    return render_template('create.html', titulo='Cadastro de preço do combustível')


@app.route('/list')
def listarPostos():
    lista = posto_dao.listar()
    return render_template('lista.html', titulo='Lista de postos cadastrados', postos=lista)


@app.route('/cadastrarPreco', methods=['POST', ])
def cadastrarPreco():
    if 'teste' == request.form['nome']:
        preco = request.form['preco']
        produto = request.form['produto']
        bairro = request.form['bairro']
        nome = request.form['nome']
        bandeira = request.form['bandeira']
        posto = Posto(preco, produto, bairro, nome, bandeira)
        posto_dao.salvar(posto)
        flash(request.form['nome'] + ' cadastrado com sucesso!')
        return redirect(url_for('listarPostos'))
    else:
        flash('Erro ao cadastrar preço, tente novamente mais tarde!')
        return redirect(url_for('index'))


app.run(debug=True)
