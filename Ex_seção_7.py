"""
Exercícios
"""
from collections import OrderedDict
from collections import Counter
# 1.0
A: list = [1, 0, 5, -2, -5, 7]
print(A)
print((A[0]+A[1]+A[5]))
A[4]: int = 100
print(A)
for x in A:
    print(x)

# 2.0
lista: list = [0, 1, 2, 3, 4, 5]
print(lista)

# 5.0
n = range(11)
for n in range(11):
    if n % 2 == 0:
        print(n)

# 6.0
vetor: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vetor[9], vetor[0])

# 7.0
vetor: list = []
for posicao in range(10):
    vetor.append(int(input(f'Leia dez valores inteiros {posicao + 1}/10: ')))
print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))

# 8.0
vetor: list = [0, 1, 2, 3, 4, 5]
vetor.reverse()
print(vetor)

# 9.0
pares: list = []
for posicao in range(6):
    pares.append(int(input(f'Leia seis valores pares {posicao + 1}: ')))
pares.reverse()
print(pares)

# 10.0
nota: list = [7, 8, 6, 9, 10, 10, 5, 6, 7, 4, 8, 7, 6, 5, 8]
media = (sum(nota)) // 15.0
print(media)

# 12.0
vetor: list = [2, 4, 6, 8, 10]
print(vetor)
print(max(vetor))
print(min(vetor))
media = (sum(vetor)) // 5.0
print(media)

# 13.0
vetor: tuple = (1, 3, 7, 8, 9)
print(max(vetor))
print(min(vetor))

# 14.0
vetor: list = []
for posicao in range(10):
    vetor.append(int(input(f'Informe o valor {posicao + 1}/10: ')))
res = Counter(vetor)
for chave, valor in res.items():
    if valor > 1:
        print(f'O valor {chave} repete {valor} vezes no vetor.')

# 15.0
vetor: tuple = (1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 11, 12, 13)
print(vetor)
vetor_2 = {1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 11, 12, 13}
print(vetor_2)

# 16.0
vetor: list = []
for posicao in range(5):
    vetor.append(int(input(f'Informe o valor {posicao + 1}/5: ')))
codigo: int = int(input('Leia um número entre 0 e 2: '))
if codigo == 0:
    print('Programa finalizado')
elif codigo == 1:
    print(vetor)
elif codigo == 2:
    print(vetor.reverse())
else:
    print('Código inválido')

# 17.0
vetor: list = []
for posicao in range(10):
    vetor.append(int(input(f'Informe o valor {posicao + 1}/10: ')))
res = Counter(vetor)
for chave, valor in res.items():
    if valor < 0:
        valor = 0
        print(f'O valor negativo {chave} se tornou {valor}.')
print(vetor)

# 21.0
A: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B: set = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
C = A - B
print(C)

# 30.0
vetor_1: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
vetor_2: set = {1, 3, 5, 7, 9, 11, 12, 15, 17, 20}
vetor_3 = vetor_1.intersection(vetor_2)
print(vetor_3)

# 31.0
vetor_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
vetor_2 = {1, 3, 5, 7, 9, 11, 12, 15, 17, 20}
vetor_3 = vetor_1.union(vetor_2)
print(vetor_3)

# 34.0
vetor: list = []
i: int = 1
tam_vetor: int = 1
num: int = int(input('Leia o primeiro número: '))
vetor.append(num)
while i <= 9:
    num = int(input(f'Digite o {i+1} número: '))

    vezes_rep: int = 0
    j: int = 0
    ind: int = 0
    while j < tam_vetor:
        if num == vetor[ind]:
            vezes_rep += 1
    ind += 1
    j += 1
    if vezes_rep == 0:
        vetor.append(num)
        tam_vetor = len(vetor)
    else:
        print('Digite um número que não seja repetido.')
        i -= 1
    i += 1
print(vetor)

# 36.0
vetor: dict = dict(a=1.0, b=2.0, c=3.0, d=4.0, e=5.0, f=6.0, g=7.0, h=8.0, i=9.0, j=10.0)
print(vetor)
vetor: dict = OrderedDict(a=1.0, b=2.0, c=3.0, d=4.0, e=5.0, f=6.0, g=7.0, h=8.0, i=9.0, j=10.0)
print(vetor)
