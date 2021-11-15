import requests


'''
Crie uma funcao que retorna True
se um professor leciona uma disciplina
e False caso contrario

Se a disciplina nao existe, retorne uma tupla: (False,'disciplina inexistente')

IMPORTANTE: essa função deve consultar o servidor definido
no controle pessoas, através da rede. Nao deve de nenhuma forma
dar import no arquivo controle pessoas ou acessar os dados
de alguma outra forma
'''


def leciona(id_professor, id_disciplina):
    r = requests.get(f'http://localhost:5000/leciona/{id_professor}/{id_disciplina}/')
    retorno = r.json()
    if retorno['isok'] is False:
        return False, 'disciplina inexistente'
    return retorno['leciona']


def aluno_ativo(nome_aluno, id_disciplina):
    r = requests.get(f'http://localhost:5000/notas/{nome_aluno}/{id_disciplina}/')
    retorno = r.json()
    if retorno['isok'] is False:
        return False, 'aluno inexistente'
    return retorno


'''
Agora, de runtests.

Se esta tudo ok, (passou testes 002a e 002b) siga para o arquivo
sistema_atividades.py

'''
# if __name__ == '__main__':
#     # r = requests.get(f'http://localhost:5050/notas/alexandre/{1}/')
#     # print(r)
#     # retorno = r.json()
#     # print(retorno)
#     # print('----' * 5)
#     # r = requests.get(f'http://localhost:5000/notas/alexandre/{1}')
#     # print(r)
#     # retorno = r.json()
#     # print(retorno)

#     # r = requests.get(f'http://localhost:5000/leciona/{1}/{2}/')
#     # print(r)
#     # retorno = r.json()
#     # print(retorno)
