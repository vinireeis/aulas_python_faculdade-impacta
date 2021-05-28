# desafio 1 hiring coders
a = 3
b = 5
c = a * b + 5
a = a + 8/2
b = 5 * b * 5 
print(a)
print(b)
print(c)

print('-' * 60)
print('-' * 60)

# desafio 2
imp = 0
x = int(input('Informe o salario:'))
if x < 1000:
    imp = 0
else:
    imp = (x - 150) * 15/100

print(imp)

# desafio 3
print('-' * 60)
print('-' * 60)

x = int(input('Informe o valor de x: '))
if x > 10:
    y = x * x
    print(y)
else:
    print('Impossível calcular')

# desafio 5 (questão 10)

num = int(input('Informe um número'))
p = 0
i = 0

while num > 0:
    if num % 2 ==0:
        p = p + 1
    else:
        i = i + 1
    num = num - 1

print (p)
print (i)

# desafio 4 questão 11

a = 2
while a < 1000:
    a = a * 2
print(a)
