arquivo = open('exercicio1.txt', 'w')

for n in range(10):
    numero = int(input('Digite um número: '))
    arquivo.write(str(numero))