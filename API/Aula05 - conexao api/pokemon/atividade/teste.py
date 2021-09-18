import requests


def nivel_do_pokemon(nome, experiencia):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome}/'.lower()
    resp = requests.get(url)
    if resp.status_code == 200:
        dic = resp.json()
        curva_url = dic['growth_rate']['url']
        resp_curva = requests.get(curva_url)
        dic_curva = resp_curva.json()
        #level = dic_curva['levels']
        for x in range(100):
            if experiencia >= int(dic_curva['levels'][x]['experience']):
                level = dic_curva['levels'][x]['level']
            print(level)

        # for x in dic_curva['levels']:

        # if experiencia <= dic_curva['levels'][x]['experience']:
        # print(dic_curva['levels'][x]['experience'])


nivel_do_pokemon(25, 5000)
