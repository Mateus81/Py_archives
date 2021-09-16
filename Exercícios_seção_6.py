"""
Exercícios
"""
from time import sleep

# 1.0
for num in range(3, 16, 3):
    print(num)

# 3.0
vetor_1: list = []
for i in range(10, -1, -1):
    vetor_1.append(i)
print(vetor_1)
print('FIM!')

# 5.0
counter: int = 1
soma: int = 0
while counter <= 10:
    soma: int = soma + counter
    counter: int = counter + 1
print(f'A adição dos valores é igual a {soma}')

# 6.0
contador: int = 1
soma: int = 0
media: float = soma / 10
while contador <= 10:
    soma = soma + contador
    contador = contador + 1
    media = soma / 10
print(f'A média dos valores é igual a {media}')

# 7.0
soma: int = 0
media: float = 0
for n in range(1, 11):
    numero: int = int(input(f'Informe o {n}/10 valor positivo: '))
    while numero < 0:
        numero: int = int(input(f'Informe o {n}/10 valor positivo: '))
    soma = soma + numero
media = soma / 10
print(f'A média de todos os valores positivos é {media}')

# 8.0
lista: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print([0], [9])

# 9.0
inteiro: int = int(input('Leia um número inteiro: '))
i: int = 0
impar: int = 1
while i < inteiro:
    print(impar)
    i = i + 1
    impar = impar + 2

# 10.0
soma: int = 0
for n in range(1, 51):
    if n % 2 == 0:
        soma = soma + n
        print(soma)

# 11.0
numero: int = int(input('Digite um número inteiro e positivo: '))

while numero < 0:
    print('O número tem que ser inteiro e positivo. ')
    numero = int(input('Digite um número inteiro e positivo: '))
for numero in range(0, numero + 1):
    print(numero)

# 12.0
numero: int = int(input('Digite um número inteiro e positivo: '))

while numero < 0:
    print('O número tem que ser inteiro e positivo. ')
    numero = int(input('Digite um número inteiro e positivo: '))
for numero in range(numero, - 1, - 1):
    print(numero)

# 17.0
soma: int = 0
numero: int = int(input('Digite um número: '))
for n in range(0, numero + 1):
    soma = soma + n
print(f'A soma é {soma}')

# 19.0
numero: int = int(input('Digite um número entre 100 e 999: '))
for posicao_digito in enumerate(numero.__str__()):
    print(posicao_digito)

# 23.0
n: int = int(input('Leia um número positivo: '))
for i in range(1, n):
    if n % i == 0:
        print(n)

# 39.0
base: float = float(input('Leia a base do triângulo: '))
altura: float = float(input('Leia a altura do triângulo: '))
area: float = base * altura / 2
print(area)

# 47.0
num1: int = int(input('Leia um número inteiro: '))
num2: int = int(input('Leia um número inteiro: '))
opcao: int = int(input('Escolha uma opção entre 1 e 5: '))
if opcao == 1:
    print(num1 + num2)
    sleep(1)
elif opcao == 2:
    print(num1 - num2)
    sleep(1)
elif opcao == 3:
    print(num1 * num2)
    sleep(1)
elif opcao == 4:
    print(num1 / num2)
    sleep(1)
elif opcao == 5:
    print('Operação Encerrada.')
    sleep(1)
    exit()
else:
    print('Você deve informar um número entre 1 e 5: ')

# 54.0
num: int = int(input('Informe um número inteiro maior que 1: '))
if num % 2 == 1:
    print('Primo')
else:
    print('Não é Primo')
