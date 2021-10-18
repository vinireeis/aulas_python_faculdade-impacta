import sqlite3

con = sqlite3.connect('dados.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS TAREFAS(id integer primary key autoincrement, nome text, descricao text, prioridade integer')

# class TodoDB:
#     def __init__(self, dados):
#         self.conexao = sqlite3.connect(dados)
#         self.cursor = self.conexao.cursor()


def listar_tudo():
    for linha in cur.execute("SELECT * FROM TAREFAS"):
        print(linha)
