from flask import Flask, jsonify

app = Flask('app')

vendedores = [
    {"nome": "Anthony", "numero": "5587991806886"},
    {"nome": "Ane", "numero": "5587991898585"},
    {"nome": "Paula", "numero": "5587991869999"}
]

indice_atual = {"valor": 0}

@app.route('/proximo-vendedor' , methods=['GET'])
def proximo_vendedor():
    vendedor = vendedores[indice_atual["valor"]]
    indice_atual["valor"] = (indice_atual["valor"] + 1) % len(vendedores)
    return jsonify(vendedor)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

