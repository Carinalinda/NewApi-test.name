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
# Rota para Ana Maria Braga
@app.route('/user/<numero>', methods=['GET'])
def pegar_usuario(numero):
    # numero = 4
    localNumber = int(numero)

    return jsonify({'users': usuarios[localNumber]})

if __name__ == '__main__':
    app.run(port=3000)