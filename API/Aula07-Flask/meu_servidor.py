from flask import Flask, jsonify, request


class AlunoNaoExiste(Exception):
    pass


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/pizzas")
# def pizzas():
#     return "mussarela, catufrango, pepperoni"
# lista = ['lucas', 'vinicius', 'thais']
# @app.route("/pessoas")
# def pessoas():
#     return jsonify(lista)


todas_pessoas = {
    "alunos": [{"nome": "beatriz", "id": 12}, {"nome": "Vinicius", "id": 11}],
    "professores": []
    }


def busca_aluno_por_id(id_aluno):
    lista_alunos = todas_pessoas['alunos']
    for aluno in lista_alunos:
        if aluno['id'] == id_aluno:
            return aluno
    raise AlunoNaoExiste


@app.route("/alunos")  # se não escrever o padrão é methods=['GET']
def get_alunos():
    return jsonify(todas_pessoas["alunos"])


@app.route("/alunos", methods=['POST'])
def post_alunos():
    dic_aluno = request.json  # {"nome":"lucas", "id":11212}
    lista_alunos = todas_pessoas["alunos"]
    lista_alunos.append(dic_aluno)
    # todas_pessoas["alunos"].append(dic_aluno)
    return jsonify(todas_pessoas["alunos"])


@app.route("/alunos/<int:id_aluno>", methods=['GET'])
def get_aluno_por_id(id_aluno):
    try:
        aluno = busca_aluno_por_id(id_aluno)
    except AlunoNaoExiste:
        return 'aluno nao encontrado', 400
    return aluno


@app.route("/reseta", methods=['POST'])
def reseta():
    todas_pessoas["alunos"].clear()
    return 'blag'


@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def delete_aluno_por_id(id_aluno):
    try:
        aluno = busca_aluno_por_id(id_aluno)
    except AlunoNaoExiste:
        return ({'erro': 'aluno nao encontrado'}, 400)
    lista_alunos = todas_pessoas['alunos']
    lista_alunos.remove(aluno)
    return aluno


@app.route("/aluno/<int:id_aluno>", methods=['PUT'])
def edita_aluno_por_id(id_aluno):
    dic_update = request.json
    try:
        aluno = busca_aluno_por_id(id_aluno)
    except AlunoNaoExiste:
        return 'aluno nao encontrado', 400
    aluno['nome'] = dic_update['nome']
    return aluno


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
