from random import randint

jogadas = []
repostas = []
cont = 0
jogo = ['Martelo', 'Plastico', 'Alicate']
y = int(input("Quantas vezes deseja jogar? "))

for i in range(y):
  jogadas.append(str(input('Escolha uma opção para jogar:\n0 - Martelo\n1 - Plastico\n2- Alicate\n')))
  jogadas.capitalize()

	if jogadas[cont] == Martelo:
		respostas.append(jogadas[cont])
	elif jogadas[cont] == Plastico:
		respostas.append(jogadas[cont])
	else:
		respostas.append("Alicate")
	cont +=1

for j in range(y):
	print(jogadas[j])