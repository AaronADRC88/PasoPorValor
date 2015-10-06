__author__ = 'aferreiradominguez'


def funcion(x, y):
    """funcion que define x e y"""
    x = x + 1
    y.append(23)
    print(x, y)
    return x


x = 22
y = [22]

funcion(x, y)
print(x, y)


def porDos(x, y):
    """retorno duas variables"""
    return x * 2, y * 2


a, b = porDos(1, 3)
print(a, b)

c = porDos(3, 4)
for n in c:
    print(n)

