from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    'Jovanna'
    'Kaua'
    'Hina'
]

@app.route('/users', methods=['GET'])
def usuarios():
    return jsonify({'message': 'oii, tudo bem?'})