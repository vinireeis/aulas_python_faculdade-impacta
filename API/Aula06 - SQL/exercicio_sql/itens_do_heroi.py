from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def heroi_tem_item(heroi_id):
    with engine.connect() as conexao:
        query = text("SELECT * FROM ItemDoHeroi WHERE idHeroi = :idHeroi")
        tapa_buraco = conexao.execute(query, idHeroi = heroi_id)
        herois = tapa_buraco.fetchall()
        if herois == []:
            return False
        else:
            return True

def heroi_quantos_itens(id_heroi):
    with engine.connect()  as conexao:
        query = text("SELECT * FROM ItemDoHeroi WHERE IdHeroi = :idHeroi")
        tapa_buraco = conexao.execute(query, idHeroi = id_heroi)
        herois = tapa_buraco.fetchone()
        cont = 0
        while herois != None:
            if dict(herois)['idHeroi'] == id_heroi:
                cont += 1
                herois = tapa_buraco.fetchone()
            else:
                break
        return cont

def itens_do_heroi(id_heroi):
    with engine.connect() as conexao:
        query = text("SELECT * FROM Item as TB1 LEFT JOIN ItemDoHeroi AS TB2 ON TB1.id = TB2.idItem WHERE idHeroi = :idHeroi")
        executa_query = conexao.execute(query, idHeroi = id_heroi)
        items_herois = executa_query.fetchall()
        return items_herois

def itens_em_uso_por_nome_do_heroi(nome_heroi):
    with engine.connect() as conexao:
        lista = []
        query = text("SELECT * FROM Item JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.idItem JOIN Heroi ON Heroi.id = ItemDoHeroi.idheroi WHERE Heroi.nome = :nome")
        exec_query = conexao.execute(query, nome = nome_heroi)
        itens_uso = exec_query.fetchall()
        for x in itens_uso:
            if x['emUso'] == 1:
                print(x)
                lista.append(dict(x))
        if len(lista) < 2: 
            print(lista)
            return lista
            
        else:
            lista = []





if __name__ == '__main__':
    itens = itens_em_uso_por_nome_do_heroi('harry')
    print(itens[0]['magia'])
    
        
