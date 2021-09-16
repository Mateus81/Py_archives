""" Exercícios - Matriz
"""
# 1.0
m: list = []
m1: list = []
contadorp: int = 0
for i in range(4):
    for j in range(4):
        m1.append(int(input('Número: ')))
    m.append(m1)
    m1: list = []
for i in m:
    for j in i:
        if j > 10:
            contadorp = contadorp + 1
print(f'Há {contadorp} números maiores que 10')
print(m)

# 2.0
m: list = []
m1: list = []
contador: int = 0
for i in range(5):
    for j in range(5):
        m1.append(int(input('Número: ')))
    m.append(m1)
    m1: list = []
for i in m:
    for j in i:
        contador = contador + 1
print(m)

# 4.0
matriz: list = []
matriz1: list = []
count: int = 0
for i in range(4):
    for j in range(4):
        matriz1.append(int(input('Número: ')))
    matriz.append(matriz1)
    matriz1: list = []
for i in matriz:
    for j in i:
        count = count + 1
maior: int = max([valor for linha in matriz for valor in linha])
print(matriz)
print(maior)
