import mysql.connector
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, static_url_path='/static')

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "Login" 
)

if conexao.is_connected():
    print("Conexão estabelecida com sucesso!")

cursor = conexao.cursor() # eu estou apontando pra alguma coisa do meu banco (tabela, banco etc). Executa a ação no banco

cursor.execute("SELECT * FROM Usuários") #exemplo de consulta

resultados = cursor.fetchall() # tras os resultados da consulta salvando na variável "resultados"

for linha in resultados:
    print(linha)

#      NECESSÁRIO ENCERRAR A CONEXÃO COM O BANCO
cursor.close()

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    # Obter os dados enviados na solicitação POST
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Usuários WHERE email = %s AND senha = %s", (email, senha))
    resultado = cursor.fetchone()  # Retorna apenas uma linha de resultado

    if resultado:
        # Se o login for bem-sucedido, retorne um status 200 com uma mensagem de sucesso
        return jsonify({'message': 'Login bem-sucedido!'}), 200
    else:
        # Se o login falhar, retorne um status 401 com uma mensagem de erro
        return jsonify({'error': 'Credenciais inválidas. Por favor, verifique seu email e senha.'}), 401

    cursor.close()  # Movido para este ponto para garantir que seja fechado após a execução da consulta

@app.route('/insert', methods=['POST'])
def insert_usuario():
    # Obter os dados enviados na solicitação POST
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    # Abrir conexão com o banco de dados
    cursor = conexao.cursor()
    
    try:
        # Executar a inserção dos dados na tabela Usuários
        cursor.execute("INSERT INTO Usuários (email, senha) VALUES (%s, %s)", (email, senha))
        conexao.commit()
        # Se a inserção for bem-sucedida, retornar uma mensagem de sucesso
        return jsonify({'message': 'Cadastro realizado com sucesso!'}), 200
        
    except mysql.connector.Error as err:
        # Se ocorrer algum erro, imprimir o erro e retornar uma mensagem de erro
        print("Erro ao inserir dados:", err)
        return jsonify({'error': 'Ocorreu um erro ao cadastrar o usuário.'}), 500
    finally:
        # Sempre fechar o cursor e a conexão após a execução
        cursor.close()

@app.route('/Cadastre-se.html')
def cadastrese():
    return render_template('cadastre-se.html')

@app.route('/FAQ.html')
def FAQ():
    return render_template('FAQ.html')



@app.route('/contact.html')
def contato():
    return render_template('contact.html')

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/secondPage.html')
def secondPage():
    return render_template('secondPage.html')

@app.route('/index1/applevision.html')
def applevision():
    return render_template('index1/applevision.html')

@app.route('/index1/iphone.html')
def iphone():
    return render_template('index1/iphone.html')

@app.route('/index1/fone.html')
def fone():
    return render_template('index1/fone.html')

@app.route('/index1/gabinete.html')
def gabinete():
    return render_template('index1/gabinete.html')

@app.route('/index1/teclado.html')
def teclado():
    return render_template('index1/teclado.html')

@app.route('/index1/mouse.html')
def mouse():
    return render_template('index1/mouse.html')

@app.route('/index1/SSD.html')
def SSD():
    return render_template('index1/SSD.html')

@app.route('/index1/xioami.html')
def xioami():
    return render_template('index1/xioami.html')
@app.route('/index1/tecladorazer.html')
def tecladorazer():
    return render_template('index1/tecladorazer.html')

@app.route('/index1/placamae.html')
def placamae():
    return render_template('index1/placamae.html')

@app.route('/index1/rtx4090.html')
def rtx4090():
    return render_template('index1/rtx4090.html')

@app.route('/index1/alexa.html')
def alexa():
    return render_template('index1/alexa.html')

@app.route('/index2/monitor.html')
def monitor():
    return render_template('index2/monitor.html')

@app.route('/index2/ps5.html')
def ps5():
    return render_template('index2/ps5.html')

@app.route('/index2/xbox.html')
def xbox():
    return render_template('index2/xbox.html')

@app.route('/index2/controleps5.html')
def controleps5():
    return render_template('index2/controleps5.html')

@app.route('/index2/controlexbox.html')
def controlexbox():
    return render_template('index2/controlexbox.html')

@app.route('/index2/watercoller.html')
def watercoller():
    return render_template('index2/watercoller.html')



if __name__ == "__main__":
    app.run(debug=True)
