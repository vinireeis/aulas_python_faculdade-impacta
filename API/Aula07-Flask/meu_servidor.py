from flask import Flask, json, jsonify, request


class AlunoNaoExiste(Exception):
    pass


class ProfessorNaoExiste(Exception):
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


def busca_professor_por_id(id_professor):
    lista_professores = todas_pessoas['professores']
    for prof in lista_professores:
        if prof['id'] == id_professor:
            return prof
    raise ProfessorNaoExiste


@app.route("/alunos")  # se não escrever o padrão é methods=['GET']
def get_alunos():
    return jsonify(todas_pessoas["alunos"])


@app.route("/alunos", methods=['POST'])
def post_alunos():
    dic_aluno = request.json  # {"nome":"lucas", "id":11212}
    if 'nome' in dic_aluno:
        lista_alunos = todas_pessoas["alunos"]
        for aluno in lista_alunos:
            if aluno['id'] == dic_aluno['id']:
                return ({'erro': 'id ja utilizada'}, 400)
        lista_alunos.append(dic_aluno)
        # todas_pessoas["alunos"].append(dic_aluno)
        # return 'adcionado com sucesso'
        return jsonify(todas_pessoas["alunos"])
    return ({'erro': 'aluno sem nome'}, 400)


@app.route("/alunos/<int:id_aluno>", methods=['GET'])
def get_aluno_por_id(id_aluno):
    try:
        aluno = busca_aluno_por_id(id_aluno)
    except AlunoNaoExiste:
        return ({'erro': 'aluno nao encontrado'}, 400)
    return aluno


@app.route("/reseta", methods=['POST'])
def reseta():
    todas_pessoas["alunos"].clear()
    return ''


@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def delete_aluno_por_id(id_aluno):
    try:
        aluno = busca_aluno_por_id(id_aluno)
    except AlunoNaoExiste:
        return ({'erro': 'aluno nao encontrado'}, 400)
    lista_alunos = todas_pessoas['alunos']
    lista_alunos.remove(aluno)
    return aluno


@app.route("/alunos/<int:id_aluno>", methods=['PUT'])
def edita_aluno_por_id(id_aluno):
    dic_update = request.json
    if 'nome' in dic_update:
        try:
            aluno = busca_aluno_por_id(id_aluno)
        except AlunoNaoExiste:
            return ({'erro': 'aluno nao encontrado'}, 400)
        aluno['nome'] = dic_update['nome']
        return aluno
    return ({'erro': 'aluno sem nome'}, 400)


@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(todas_pessoas['professores'])


@app.route("/professores/<int:id_professor>", methods=['GET'])
def get_professor_por_id(id_professor):
    try:
        prof = busca_professor_por_id(id_professor)
    except ProfessorNaoExiste:
        return ({'erro': 'professor nao encontrado'}, 400)
    return prof


@app.route("/professores", methods=['POST'])
def post_professores():
    dic_professor = request.json
    if 'nome' in dic_professor:
        dic_professores = todas_pessoas['professores']
        for prof in dic_professores:
            if prof['id'] == dic_professor['id']:
                return ({'erro': 'id ja utilizada'}, 400)
        dic_professores.append(dic_professor)
        return jsonify(todas_pessoas['professores'])
    return ({'erro': 'professor sem nome'}, 400)


@app.route("/professores/reseta", methods=['POST'])
def reseta_professores():
    todas_pessoas['professores'] = []
    return 'dados de professores resetados'


@app.route("/professores/<int:id_professor>", methods=['DELETE'])
def deleta_prof_por_id(id_professor):
    try:
        prof = busca_professor_por_id(id_professor)
        lista_prof = todas_pessoas['professores']
        lista_prof.remove(prof)
        return jsonify(lista_prof)
    except ProfessorNaoExiste:
        return ({'erro': 'professor nao encontrado'}, 400)


@app.route("/professores/<int:id_professor>", methods=['PUT'])
def edita_prof_por_id(id_professor):
    dic_prof = request.json
    if 'nome' in dic_prof:
        try:
            prof = busca_professor_por_id(id_professor)
        except ProfessorNaoExiste:
            return ({'erro': 'professor nao encontrado'}, 400)
        prof['nome'] = dic_prof['nome']
        return prof
    return ({'erro': 'professor sem nome'}, 400)

# @app.route("/professores", methods=['POST'])
# def post_professores():
#     dic_professor = request.json if request.json['nome'] is not None else False
#     if dic_professor:
#         dic_professores = todas_pessoas['professores']
#         for professor in dic_professores:
#             if professor['id'] == dic_professor['id']:
#                 return ({'erro': 'id ja utilizada'}, 400)
#         dic_professores.append(dic_professor)
#         return jsonify(todas_pessoas['professores'])
#     return ({'erro': 'aluno sem nome'}, 400)


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
