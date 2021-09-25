from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')
# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui
def heroi_existe(id_heroi):
    with engine.connect() as con:
        statement = text ("SELECT * FROM Heroi WHERE id = :heroi") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        retorno = con.execute(statement, heroi=id_heroi) #e usei esse buraco
        heroi = retorno.fetchone()                   #pega a primeira linha do resultado
        if heroi == None:                       #se nao tinha nenhuma linha, 
                                                  #jogador vale None
                                                  # (None tb aparece quando a gente
                                                  # já leu várias linhas e acabou 
                                                  # a consulta)
            return False
        return True

def consultar_heroi(id_heroi):
    with engine.connect() as conexao:
        statement = text ("SELECT * FROM Heroi WHERE id = :heroi") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        retorno = conexao.execute(statement, heroi=id_heroi) #e usei esse buraco
        herois = retorno.fetchall()                   #pega a primeira linha do resultado
        if herois == []:
            raise HeroiNaoExisteException
        else:
            herois = herois[0]
            return dict(herois)


