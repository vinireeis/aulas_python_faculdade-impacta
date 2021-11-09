database = {}
database['PESSOAS'] = [{"nome": "lucas", "id": 12},
                       {"nome": "beatriz", "id": 13}]


class NotFoundError(Exception):
    pass


# Assim, poderemos adicionar pessoas: i.adiciona_pessoa({'nome':'fernando','id':1})
# Pegar a lista de todas as pessoas : i.todas_as_pessoas()
# Consultar uma pessoa por id       : i.localiza_pessoa(1) (retorna o dicionario do fernando)
# Tb queremos uma função reseta.    : i.reseta() faz a lista de pessoas ficar vazia
def todas_as_pessoas():
    return database["PESSOAS"]


def localiza_pessoa(id_pessoa):
    for pessoa in database["PESSOAS"]:
        if pessoa['id'] == id_pessoa:
            return pessoa
    raise NotFoundError


def reseta():
    database["PESSOAS"] = []
    return 'r'


def adiciona_pessoa(dic_pessoa):
    database["PESSOAS"].append(dic_pessoa)
    return database["PESSOAS"]


if __name__ == '__main__':
    print(database)
    x = adiciona_pessoa({"nome": "Vinicius", "id": 5})
    print(x)

# Quais as funções que tem que ser feitas pra essa parte?
# adiciona_interesse(id1,id2) : marca que 1 quer falar com 2
# consulta_interesses(id1)    : devolve a lista de todos os interesses de 1
# remove_interesse(id1,id2)   : marca que 1 não quer mais falar com 2
# Detalhes:
# * Essas funções devem verificar se o usuário não é válido. Se for o caso,
# devem lançar a excessão NotFoundError
# * O reseta também deve funcionar para apagar os interesses

# database['interesses'] = {
#     100: [101, 102, 103,40],
#     200: [100],
#     30 : []
# }


def adiciona_interesse():  # (100,40)
    pass


def consulta_interesses():
    pass


#  essa funcao só vai ser testada
#  quando estivermos fazendo matches
def remove_interesse():
    pass


def lista_matches():
    pass
