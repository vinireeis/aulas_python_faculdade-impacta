import random

cont_index = -1
lista = [0, 1]
lista1 = []
for x in range(11):
  sort = random.choice(lista)
  if sort == 0:
    lista1.append("A")
    print(lista1[0])
  else:
    lista1.append("B")
    print("B")
