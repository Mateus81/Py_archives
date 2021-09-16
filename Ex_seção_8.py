"""
Exercicios
"""
from statistics import sqrt

# 1.0
numero: int = int(input('Digite um número inteiro: '))


def dobro_de_um_inteiro() -> None:
    print(numero * 2)


dobro_de_um_inteiro()


# 2.0
def data() -> None:
    print('14/07/2020')
    print('14 de Julho de 2020')


data()

# 3.0
numero: int = int(input('Digite um número: '))


def numeros(n):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    return 0


print(numeros(numero))

# 4.0
numero: int = int(input('Digite um número: '))


def quadrado_perfeito():
    if numero > 0:
        return numero * numero
    return f'Não podemos calcular o quadrado perfeito desse numero: {numero}'


print(quadrado_perfeito())


# 5.0


def calcula_volume(raio):
    pi: float = 3.14
    v: float = 4 / 3 * pi * raio ** 3
    return v


print(calcula_volume(2))


# 6.0
def conversao(horas, minutos, segundos):
    return horas * 3600, minutos * 60, segundos * 1


print(conversao(7, 20, 40))


# 7.0


def temperatura() -> float:
    c = float(input('Digite a temperatura em Celsius: '))
    f = c * (9.0 + 5.0) + 32.0
    return f


print(f'A temperatura Celsius convertida em Fahrenreit é {temperatura()}')

# 8.0

a: int = int(input('Digite o valor do cateto: '))
b: int = int(input('Digite o valor do cateto: '))
h = sqrt(a ** 2 + b ** 2)


def hipotenusa():
    return sqrt(a ** 2 + b ** 2)


print(hipotenusa())

# 9.0
h: float = float(input('Digite a altura do cilindro: '))
r: float = float(input('Digite o raio do cilindro: '))
v = 3.14 * r ** 2 * h


def volume_cilindro(v):
    return 3.14 * r ** 2 * h


print(volume_cilindro(f'O volume do cilindro é {v}'))

# 10.0
num1: int = int(input('Digite um número: '))
num2: int = int(input('Digite um número: '))


def maior_numero():
    if num1 > num2:
        print(f'O {num1} é o maior')
    elif num2 > num1:
        print(f'O {num2} é o maior')


print(maior_numero())

# 11.0
n1: float = float(input('Digite a primeira nota: '))
n2: float = float(input('Digite a segunda nota: '))
n3: float = float(input('Digite a terceira nota: '))
letra: str = str(input('Calcule:\nA - para Media Aritmetica\nP - para Media Ponderada: ')).upper()


def notas(n1, n2, n3, letra):
    if letra == 'A':
        c1 = n1 + n2 + n3 / 3
        return f'A Média aritmética é: {c1}'
    c2 = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    return f'A sua Media Ponderada e: {c2}'


print(notas(n1, n2, n3, letra))

# 12.0
inteiro: int = int(input('Leia um número inteiro maior que zero: '))


def operacao():
    global inteiro
    soma: int = 0
    while inteiro > 0:
        soma += inteiro % 10
        inteiro = inteiro // 10
    print(soma)
    if inteiro < 0:
        print('Número Inválido')


operacao()

# 13.0
num1: int = int(input('Leia um número inteiro: '))
num2: int = int(input('Leia outro número inteiro: '))
simbolo: str = input('Leia o símbolo da operação: ')


def op():
    if simbolo == '+':
        return num1 + num2
    elif simbolo == '-':
        return num1 - num2
    elif simbolo == '*':
        return num1 * num2
    elif simbolo == '/':
        return num1 / num2


print(op())

# 14.0
km: int = int(input('Leia quantos quilometros o carro andou: '))
kml: int = int(input('Quantos litros consumiu?: '))


def consumo():
    if kml < 8:
        return 'Venda o carro!'
    elif kml > 8 < 14:
        return 'Econômico!'
    elif kml > 12:
        return 'Super Econômico!'


print(consumo())

# 16.0
l: int = int(input('Leia o número de sinais: '))


def desenha_linha(l):
    vetor_linhas: list = ['='] * l
    print(''.join(vetor_linhas))


desenha_linha(l)


# 17.0
def soma(*args):
    return sum(args)


print(soma(2, 4))


# 18.0
def funcao(x, z):
    return x ** z


print(funcao(3, 2))

# 20.0
num: int = int(input('Leia um número inteiro positivo: '))
fatorial: int = 1
contador: int = 1
while contador <= num:
    fatorial = fatorial * contador
    contador = contador + 1

print(f'O número {num} é {fatorial} fatorial')


# 22.0
def function(number):
    if number == 1:
        return '!'
    elif number == 2:
        return '!\n !!'
    elif number == 3:
        return '!\n !!\n !!!'
    elif number == 4:
        return '!\n !!\n !!!\n !!!!'
    elif number == 5:
        return '!\n !!\n !!!\n !!!!\n !!!!!'
    else:
        return 'Entrada não permitida'


print(function(5))
print(function(3))


# 23.0
def func(numero):
    result: str = ''
    lista = [n * '*' for n in range(1, numero + 1)]
    for i in range((2 * numero - 1)):
        if i < 4:
            result = result + lista[i] + '\n'
        else:
            result = result + lista[2 - i] + '\n'
    return result


print(func(4))

# 24.0
a: int = int(input('Leia um valor n positivo: '))
"""
for i in range(1, n + 1):
    triangulo = ('' * (n - 1)) + ('*' * (2 * i - 1))
    print(triangulo)
"""


def tri(n=6):
    list(print(' ' * (n - i) + ('*' * (2 * i - 1))) for i in range(1, n + 1))


tri(a)

# 25.0
n: int = int(input('Digite um número inteiro: '))
s = 2 / 4 + 5 / 5 + 10 / 6 + (n ** 2 + 1) / (n + 3)


def operacao() -> int:
    return s


print(operacao())

# 26.0
n: int = int(input('Leia um número inteiro e positivo: '))
soma: int = 0
i: int = 1
while i <= n:
    soma = soma + i
    i = i + 1

print(f'A soma dos {n} primeiros números é {soma}')


# 33.0
def fatorial(n):
    if n == 0:
        return 1
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def soma(fat):
    return sum([int(i) for i in str(fat)])


n: int = int(input('Entre com um valor: '))
fat = fatorial(n)
s = soma(fat)
print(f'{n}! = {fat}')
print(f'Soma dos algarismos de {fat} = {s}')


# 34.0
def fatorial_duplo(x):
    num: int = 1
    while True:
        if x % 2 != 0:
            num *= x
        x -= 1
        if x < 1:
            break
    print(num)


fatorial_duplo(3)
fatorial_duplo(10)


# 40.0
def pares():
    contador_par: int = 0
    for i in range(6):
        entrada: int = int(input('Leia um número: '))
        numero = int(entrada)
        if numero % 2 == 0:
            contador_par += 1
    return contador_par


print(pares())


# 41.0
def maior_valor() -> None:
    print(max(2, 4, 6, 7, 8))


maior_valor()

# 66.0
caractere: str = str(input('Digite um caractere qualquer: '))
print(caractere.upper())


# 67.0
def getchar():
    caractere: str = input('Informe um caractere: ')
    return caractere


def rotina(vetor, tamanho):
    for _ in range(tamanho):
        valor = getchar()
        if valor != '':
            vetor.append(valor)
        else:
            break
    print(vetor)


v: list = []
tam: int = 5

rotina(v, tam)


# 71.0
def ponto_p(x, y, p):
    if p[0] == p[1]:
        return f'Isto é um quadrado'
    elif p[0] <= x and p[1] <= y:
        return 1
    else:
        return 0


v1: int = int(input('Informe o valor da vértice inferior do retângulo: '))
v2: int = int(input('Informe o valor da vértice superior do retângulo: '))
ponto = input('Informe a coordenada que será verificada se está dentro do retângulo no formato X,Y:')
p1, p2 = ponto.split(',')
z: list = [int(p1), int(p2)]
print(ponto_p(v1, v2, z))
