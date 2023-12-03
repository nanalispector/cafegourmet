from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__, static_url_path='/static')

# Configuração do banco de dados
app.config['DATABASE'] = 'vitrinecafe.db'

def get_db_connection():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection

def query_db(query, args=(), one=False):
    with get_db_connection() as connection:
        cursor = connection.execute(query, args)
        results = cursor.fetchall()
        return (results[0] if results else None) if one else results

@app.route('/get_products', methods=['GET'])
def get_products():
    produtos = query_db('SELECT * FROM produtos')
    return jsonify([dict(produto) for produto in produtos])

@app.route('/produto/<int:idProduto>')
def detalhes_produto(idProduto):
    # Obtenha os detalhes do produto com base no idProduto
    produto = query_db('SELECT * FROM produtos WHERE idProduto = ?', (idProduto,), one=True)
    return render_template('descricao_produto.html', produtos=[produto])

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/')
def index():
    produtos = query_db('SELECT * FROM produtos')
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
