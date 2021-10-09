from sqlalchemy import text
from sqlalchemy import create_engine
from itens import consultar_item
from itens_do_heroi import itens_em_uso_por_nome_do_heroi
from herois import consultar_heroi_por_nome
engine = create_engine('sqlite:///rpg.db')


def itens_em_uso_por_nome_do_heroi(nome_heroi):
    with engine.connect() as conexao:
        lista = []
        query = text(
            "SELECT * FROM Item JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.idItem JOIN Heroi ON Heroi.id = ItemDoHeroi.idheroi WHERE Heroi.nome = :nome")
        exec_query = conexao.execute(query, nome=nome_heroi)
        itens_uso = exec_query.fetchall()
        for x in itens_uso:
            if x['emUso'] == 1:
                lista.append(consultar_item(x['idItem']))
        if len(lista) < 2:
            return lista
        else:
            lista = []

def heroi_pronto_por_nome(nomeHeroi):
    item = itens_em_uso_por_nome_do_heroi(nomeHeroi)
    heroi = consultar_heroi_por_nome(nomeHeroi)
    heroi['vida'] = heroi['fisico'] * 10
    print(item)
    print()
    print(heroi)
    if item != []:
        heroi['magia'] += item[0]['magia']
        heroi['agilidade'] += item[0]['agilidade']
    return heroi


if __name__ == '__main__':
    #print(itens_em_uso_por_nome_do_heroi("harry"))
    heroi_pronto_por_nome('harry')
