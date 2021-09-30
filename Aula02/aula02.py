'''
    EXERCÍCIO 1:
    Implemente a função 'quadrado' que recebe um número e retorna o resultado
    desse número ao quadrado.
    Lembre-se que a função deve utilizar a instrução return, para devolver
    o resultado. Se você utilizar print dentro da função para mostrar o
    resultado, a sua função estará incorreta.
'''


def quadrado(a):
    return a * a


def soma_dos_quadrados1(a, b):
    return a * a + b * b


def quadrado1(a):
    b = a * a
    return b


'''
EXERCÍCIO 2:
    Implmente a função 'soma_dos_quadrados' que receba dois numeros e devolve
    a soma dos seus quadrados.
    Você pode utilizar a função 'quadrado' definida anteriormente para
    facilitar a implementação.
'''


def soma_dos_quadrados(a, b):
    return quadrado(a) + quadrado(b)


'''
EXERCÍCIO 3:
    Implemente a função 'media', que recebe três valores numéricos e retorna
    a média dos valores.
'''


def media(a, b, c):
    m = (a + b + c) / 3
    return m


'''def media1(a, b, c):
    return (a + b + c) /3'''

'''
EXERCÍCIO 4:
    Implemente a função 'calcular_salario', que recebe o salário atual de um
    funcionário e retorna o salário com um reajuste de aumento, sendo que:
    - Caso o salário atual seja maior que R$ 2.000,00, o funcionário receberá
      7% de aumento.
    - Caso contrário, o funcionário receberá 15% de aumento.
'''
# exercicio 4 calcular_salario salario + reajuste, se salario >2.000  + 7% se
#  menor + 15%


def calcular_salario(salario):
    if salario > 2000:
        reajuste_sal = salario * 1.07
        return reajuste_sal  # o return pode ser fora do if else #
    else:  # não coloquei regra pois tudo que não for 2000 é + 15%)#
        reajuste_sal = salario * 1.15
        return reajuste_sal


def calcular_salario1(salario):
    if salario > 2000:
        total = salario * 1.07
        # total = salario * 0.07 + salario
    else:
        total = salario * 1.15
        # total  = salario * 0.15 + salario
    return total


'''
Exercicio 5
    implemente a função "soma_divisores" que recebe como parametro de entrada
    um numero
    positivo e retorna a soma de todos os divisores desse número.
    Exemplo:
    - caso o número seja 15, o retorno deve ser 24 (1+3+5+15)
    - caso o número seja 30, o retorno deve ser 72 (1+2+3+5+6+10+15+30)
'''


def soma_divisores(n):
    soma = 0  # variavel para somar os divisores#
    a = 1
    while a <= n:
        if n % a == 0:  # se o meu N for divisivel sem resto#
            soma += a   # soma = soma + a
        a += 1
    return soma


def soma_divisores1(n):  # for
    soma = 0  # variavel para somar os divisores#
    for a in range(1, n + 1):  # nao precisa de variavel contador a = 1 //
        # precisa colocar n +1 pois range para 1 numero antes de N
        if n % a == 0:  # se o meu N for divisivel sem resto
            soma += a  # soma = soma + a
        a += 1
    return soma


'''
exerc 6
implemente a função fatorial que recebe um número positivo e retorna o fatorial
desse numero.
o fatorial desse número N é o produto dos números naturais consecutivos de 1
até N.
por exemplo:
- o fatorial de 5 é 120 (1*2*3*4*5)
- o fatorial de 10 é 3628800 (1*2*3*4*5*6*7*8*9*10)
'''


def fatorial(n):
    fat = 1  # soma incial em 0 multiplicador inicia em 1
    for a in range(1, n + 1):
        fat *= a  # fat = fat * a
    return fat


def fatorial1(n):  # while
    x = 1
    a = 1
    while a <= n:
        x *= a  # x = x * a #
        a += 1
    return x
