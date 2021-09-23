from pokemonmeu import PokemonNaoExisteException
import requests
"""

def nivel_do_pokemon(nome, experiencia):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        curva_url = dic['growth_rate']['url']
        resp_curva = requests.get(curva_url)
        dic_curva = resp_curva.json()
        #  level = dic_curva['levels']
        for x in range(100):
            if experiencia >= int(dic_curva['levels'][x]['experience']):
                level = dic_curva['levels'][x]['level']
            print(level)

        # for x in dic_curva['levels']:

        # if experiencia <= dic_curva['levels'][x]['experience']:
        # print(dic_curva['levels'][x]['experience'])


nivel_do_pokemon(25, 5000)



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
        print(f'EVOLUCAO ANTERIOR: {evolution_before}')
        resp = requests.get(url_evolution)
        if resp.status_code == 200:
            dic = resp.json()
            print(finals_evolves)
            if evolution_before is None and dic['chain']['evolves_to'] == []:
                print('Estou retornando lista vazia')
                return []
            for x in dic['chain']['evolves_to'][0]['evolves_to']:
                finals_evolves.append(
                    x['species']['name'] if x is not None else None)
            if evolution_before is not None and nome.lower() not in finals_evolves:
                for x in dic['chain']['evolves_to'][0]['evolves_to']:
                    evolucoes.append(x['species']['name'])
                    print(evolucoes)
                return evolucoes
            elif evolution_before is None:
                for x in dic['chain']['evolves_to']:
                    evolucoes.append(x['species']['name'])
                print(evolucoes)
                return evolucoes
            else:
                return []
        else:
            raise PokemonNaoExisteException
    else:
        raise PokemonNaoExisteException


print(evolucoes_proximas("CHARIZARD"))


'''
for x in dic['chain']['evolves_to']:
        evolucoes.append(dic[x]['species']['name'])
        #  evolucoes.append(dic[x]['species']['name'] if dic[x]['species']['name'] is not None else None)
elif dic['chain']['evolves_to']['0']['evolves_to']['0']['species']['name']:
    for x in dic['chain']['evolves_to']['0']['evolves_to']:
        evolucoes.append(dic[x]['species']['name'])
print(evolucoes)


-----------------------------===---------------------------
if dic['chain']['evolves_to'][0]['species']['name'] is not None and dic['chain']['evolves_to'][0]['species']['name'] != evolution_before and evolution_before is None:
                for x in dic['chain']['evolves_to']:
                    evolucoes.append(x['species']['name'])
                    # evolucoes.append(dic[x]['species']['name'])
            elif dic['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'] is not None and dic['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'] != nome:
                for x in dic['chain']['evolves_to'][0]['evolves_to']:
                    evolucoes.append(x['species']['name'])
            else:
                evolucoes = []
                return evolucoes
'''
