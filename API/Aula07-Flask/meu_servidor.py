from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/pizzas")
def pizzas():
    return "mussarela, catufrango, pepperoni"


lista = ['lucas', 'vinicius', 'thais']


@app.route("/pessoas")
def pessoas():
    return jsonify(lista)


todas_pessoas = {
    "alunos": [{"nome": "beatriz", "id": 12}, {"nome": "Vinicius", "id": 11}],
    "professores": []
    }


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
    if (id_aluno >= 1000 * 1000):
        return ('use apenas nros menores que 1 milhão', 400)
    for aluno in todas_pessoas["alunos"]:
        if aluno['id'] == id_aluno:
            return aluno


@app.route("/reseta", methods=['POST'])
def reseta():
    todas_pessoas["alunos"].clear()
    return 'bla'


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
