import unittest
import json
from pprint import pprint
'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirao) para estudar como acessar listas,
dicionarios,
e estruturas encadeadas (listas dentro de dicionários
dentro de listas)

Os dados estão fornecidos em um arquivo (ano2018.json) que você
pode abrir no firefox, para tentar entender melhor (use o menu
do canto direito superior, e "abrir arquivo")
'''

'''
DICA VSCODE: para poder executar o arquivo py a partir do VSCODE,
é importante ter aberto a pasta certa

Se voce tem a seguinte estrutura de diretorios
distribuidos > brasileirao > brasileirao.py
                             ano2018.json

Deve selecionar no VSCODE File > Open folder
e escolher a pasta brasileirao.
Se escolher distribuidos, o python nao vai achar o arquivo ano2018.json
'''

'''
Se quiser ver os dados dentro do python,
pode chamar a funcao
pega_dados

Nao se preocupe com como ela foi definida, ela só está
lendo o arquivo json pra voce
'''


def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados


'''
não dá muito certo imprimir todos os dados, porque o python
dá pau ao imprimir tanta coisa, mas podemos ver algumas coisas.

Descomente cada um dos exemplos abaixo para ver o que ele faz.
Verifique a correspondencia do que está sendo impresso pelo
python com o que aparece no firefox
'''
dados2018 = pega_dados()

#  print('todas as chaves do dicionario principal', dados2018.keys())

#  print('dados do time corinthians')
pprint(dados2018['equipes']['6'])

#  pprint(dados2018['equipes'])
#  print('esses foram os dados de todos os times')
#  print('repare que cada time tem uma id. A id do corintians é 6')

#  print('faixas de classificacao e rebaixamento')
#  pprint(dados2018['fases']['2700']['faixas-classificacao'])

print('classificacao dos times no fim do campeonato')
#  print(dados2018['fases']['2700']['classificacao']['grupo']['Único'])
#  print(dados2018['fases']['2700']['classificacao'])

'''
Como você viu nos prints acima, cada time tem uma id numérica,
e pode ser acessado em dados['equipes'][id_numerica]

A primeira funcao a fazer
recebe a id_numerica de um time e deve retornar
seu 'nome-comum'

Observe que essa funcao (e todas as demais!) recebem os dados dos
jogos numa variavel dados. Essa variavel
contem todas as informacoes do arquivo
json que acompanha essa atividade
'''


def nome_do_time(dados, id_numerica):
    return dados['equipes'][id_numerica]['nome-comum']


'''
A proxima funcao recebe somente o dicionario dos dados do brasileirao

Ela retorna a id do time que foi campeao.
'''


def id_campeao(dados):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0]


'''
A proxima funcao recebe somente o dicionario dos dados do brasileirao

Ela retorna o nome-comum do time que foi campeao.
'''


def nome_campeao(dados):
    campeao = id_campeao(dados)
    return nome_do_time(dados, campeao)


'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela retorna o nro de times que o brasileirao qualifica para a libertadores

Note. Esse numero está nos dados que eu forneci. Voce deve pegar dos
dados. Nao basta retornar o valor correto, tem que acessar os dados
fornecidos.

Dica: voce vai pegar uma string do tipo "1-5" do dicionário.
Pode ser util quebrar ela em duas usando string.split, e converter
as strings "1" e "5" em números inteiros
>>> string = '1-5'
>>> string.split('-')
['1', '5']
>>> string.split('-')[1]
'5'

'''


def qtos_libertadores(dados):
    classificado = dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    return int(classificado.split('-')[1])


'''
A proxima funcao recebe um tamanho, e retorna uma lista
das ids dos times melhor classificados.

O tamanho da lista que deve ser retornada é o argumento "numero_de_times"
'''


def ids_dos_melhor_classificados(dados, numero_de_times):
    lista = list()
    for x in range(0, numero_de_times):
        lista.append(dados['fases']['2700']
                     ['classificacao']['grupo']['Único'][x])
    return lista


'''
A proxima funcao usa as duas anteriores para retornar uma
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro

Lembre-se de consultar a estrutura, tanto para obter a classificacao, quanto
para obter o nro correto de times a retornar

A funcao so recebe o dicionario de dados do brasileirao

'''


def classificados_libertadores(dados):
    return ids_dos_melhor_classificados(dados, qtos_libertadores(dados))


'''
Usando as duas funcoes anteriores, podemos fazer uma que retorna os nomes dos
classificados
'''


def nomes_classificados_libertadores(dados):
    lista_nomes = []
    for time in classificados_libertadores(dados):
        lista_nomes.append(nome_do_time(dados, time))


def data_de_um_jogo(dados, id_jogo):
    for x in dados['fases']['2700']['jogos']['id']:
        if x == id_jogo:
            print(dados['fases']['2700']['jogos']['id'][x]['data'])
        else:
            print('nao encontrado')


f = pega_dados()

data_de_um_jogo(f, '102132')
