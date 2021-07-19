arquivo = open('exercicio.txt', 'w')

for n in range(10):
    numero = int(input("Digite um número inteiro: ")
    arquivo.write(str(numero))