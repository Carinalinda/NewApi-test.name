from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

usuarios = [
    'Jovanna',
    'Kaua',
    'Tina',
    'Tapioca',
    'Leide Laura',
]

@app.route('/users', methods=['GET'])
def pegar_usuarios():
    return jsonify({'users': usuarios})

# Rota para usuario pelo numero 
@app.route('/user/<numero>', methods=['GET'])
def pegar_usuario(numero):
    
    localNumber = int(numero)

    return jsonify({'users': usuarios[localNumber]})

# Rota p cadastra novo usuario
@app.route('/user', methods=['POST'])
def add_novo_usuario():
    dados = request.json
    print(dados) 
    return jsonify({
        'user': dados,
    })

if __name__ == '__main__':
    app.run(port=3000)