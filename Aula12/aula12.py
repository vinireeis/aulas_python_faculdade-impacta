# abrindo arquivos, leitura/escrita/append

arq1 = open(r'G:\Meu Drive\python\Faculdade Python\Aula12\facul.txt', 'r', encoding='UTF-8')
texto = arq1.read()
print(texto)

arq2 = open(r'G:\Meu Drive\python\Faculdade Python\Aula12\teste.txt', 'r', encoding='UTF-8')
for linha in arq2:
    print(linha)
