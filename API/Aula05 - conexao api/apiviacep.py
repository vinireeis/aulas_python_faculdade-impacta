import requests

cep = '03732-010'
url = f'http://viacep.com.br/ws/{cep}/json'
retorno = requests.get(url)  # conecetei na url e baixei o que tinha
dici = retorno.json()  # pega o conteudo, se for um json, carrega ele para o
# python > criando um dicionário ou lista, dependendo da informação que >
#  continha no endereço

logradouro = dici['logradouro']
cidade = dici['localidade']
print(f'{logradouro} - {cidade}')
retorno.status_code


def pega_rua(cep):
    url = f'http://viacep.com.br/ws/{cep}/json'
    resultado = requests.get(url)  # conecetei na url e baixei o que tinha
    if resultado.status_code != 200:
        return 'deu ruim'
    dici = resultado.json()  # pega o conteudo, se for um json, carrega ele
#  para o python > criando um dicionário ou lista, dependendo da informação que
#  continha no endereço
    '''logradouro = dici['logradouro']
    cidade = dici['localidade']
    print(f'{logradouro} - {cidade}')