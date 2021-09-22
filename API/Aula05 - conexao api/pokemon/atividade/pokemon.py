import requests
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar o treinador e os testes no documento
entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta
função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse
parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então
esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos
em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower()
e upper() da classe string.
6. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e
devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/
"""

"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no
PokeAPI, respectivamente.
"""
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "https://pokeapi.co"

"""
Vamos precisar destas quatro exceções personalizadas.
Abaixo, criamos excessões com nomes personalizados.
"""


class PokemonNaoExisteException(Exception):
    pass  # nao faça nada aqui nem nas Exceptions seguintes
    # ela já está pronta, só é um "nome" novo


class PokemonNaoCadastradoException(Exception):
    pass


class TreinadorNaoCadastradoException(Exception):
    pass


class PokemonJaCadastradoException(Exception):
    pass


"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma
ValueError se não for.
"""


def check_int(a):
    if type(a) is not int:
        raise ValueError()


"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia
e lança uma ValueError se não for.
"""


def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()


dic_cores = {
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}

dic_tipos = {
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}

"""
1. Dado o número de um pokémon, qual é o nome dele?
"""


def nome_do_pokemon(numero):
    url = f'https://pokeapi.co/api/v2/pokemon/{numero}/'
    resp = requests.get(url)
    dic = resp.json()
    return dic['name']


"""
2. Dado o nome de um pokémon, qual é o número dele?
"""


def numero_do_pokemon(nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        return dic['id']
    else:
        raise PokemonNaoExisteException


"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês)
predominante dele?
"""


def color_of_pokemon(nome):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        return dic['color']['name']
    else:
        raise PokemonNaoExisteException


"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português)
predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul",
"rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode
dar um jeito nisso?
"""


def cor_do_pokemon(nome):
    cor_traducao = color_of_pokemon(nome)
    return dic_cores[cor_traducao]


"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador",
"veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água",
"grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista
contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""


def tipos_do_pokemon(nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        tipos = []
        for x in (dic['types']):
            tipos.append(dic_tipos[x['type']['name']])
        return tipos
    else:
        raise PokemonNaoExisteException


"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo,
evolucao_anterior('bulbasaur') == None
"""


def evolucao_anterior(nome):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        return dic['evolves_from_species']['name'] if dic['evolves_from_species'] is not None else None
    else:
        raise PokemonNaoExisteException


"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo
de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais
tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa.
Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evolutivo.
Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo,
evolucoes_proximas('celebi') == []

O exercicio 7 é opcional e bastante dificil. Se quiser, desligue os testes e
vá para o 8!
"""


def evolucoes_proximas(nome):
    finals_evolves = []
    evolucoes = []
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        url_evolution = dic['evolution_chain']['url']
        evolution_before = dic['evolves_from_species']['name'] if dic['evolves_from_species'] is not None else None
        resp = requests.get(url_evolution)
        if resp.status_code == 200:
            dic = resp.json()
            if not evolution_before and dic['chain']['evolves_to'] == []:
                return []
            for x in dic['chain']['evolves_to'][0]['evolves_to']:
                finals_evolves.append(
                    x['species']['name'] if x is not None else None)
            if evolution_before is not None and nome.lower() not in finals_evolves:
                for x in dic['chain']['evolves_to'][0]['evolves_to']:
                    evolucoes.append(x['species']['name'])
                return evolucoes
            elif evolution_before is None:
                for x in dic['chain']['evolves_to']:
                    evolucoes.append(x['species']['name'])
                return evolucoes
            else:
                return []
        else:
            raise PokemonNaoExisteException
    else:
        raise PokemonNaoExisteException


"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base
na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente
(na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência,
retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
dica: na URL pokemon-species, procure growth rate
"""


def nivel_do_pokemon(nome, experiencia):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        curva_url = dic['growth_rate']['url']
        resp_curva = requests.get(curva_url)
        dic_curva = resp_curva.json()
        for x in range(100):
            if experiencia >= int(dic_curva['levels'][x]['experience']):
                level = dic_curva['levels'][x]['level']
        return level
    else:
        raise PokemonNaoExisteException
