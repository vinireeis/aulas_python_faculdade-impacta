from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')
# Essa classe só representa uma exception com
# novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)


class HeroiNaoExisteException(Exception):
    pass

# escreva suas funcoes aqui


def heroi_existe(id_heroi):
    with engine.connect() as con:
        statement = text("SELECT * FROM Heroi WHERE id = :heroi")
# :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
# :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        retorno = con.execute(statement, heroi=id_heroi)  # e usei esse buraco
        heroi = retorno.fetchone()  # pega a primeira linha do resultado
        if heroi == None:  # se nao tinha nenhuma linha,
            # jogador vale None
            # (None tb aparece quando a gente
            # já leu várias linhas e acabou
            # a consulta)
            return False
        return True


def consultar_heroi(id_heroi):
    with engine.connect() as conexao:
        statement = text("SELECT * FROM Heroi WHERE id = :heroi")
        retorno = conexao.execute(statement, heroi=id_heroi)
        herois = retorno.fetchall()
        if herois == []:
            raise HeroiNaoExisteException
        else:
            herois = herois[0]
            return dict(herois)


def consultar_heroi_por_nome(nome_heroi):
    with engine.connect() as conexao:
        consulta_db = text("SELECT * FROM Heroi WHERE nome = :heroi")
        retorno = conexao.execute(consulta_db, heroi=nome_heroi)
        nomes_heroi = retorno.fetchall()
        if nomes_heroi == []:
            raise HeroiNaoExisteException
        else:
            nomes_heroi = nomes_heroi[0]
            return dict(nomes_heroi)

# def atacar_com_fisico(atacante, defensor):
# defensor['vida'] = atacante['fisico'] - defensor['vida']


'''x = consultar_heroi_por_nome('harry')
x['vida'] = x['fisico'] * 10
print(x)'''
