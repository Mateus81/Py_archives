"""
Exercícios
"""
from typing import List, Any

# 1.0
valor: int = 7
print(valor)
print(type(valor))

# 2.0
valor: float = 1.44
print(valor)
print(type(valor))

# 3.0
valor = 4
valor1 = 3
valor2 = 3
total = (valor + valor1 + valor2)
print(total)
print(type(total))

# 4.0
valor: float = 1.44 * 1.44
print(valor)
print(type(valor))

# 5.0
valor: float = 1.44 / 5
print(valor)
print(type(valor))

# 6.0
C: int = 10
F: float = C * (9.0/5.0) + 32.0
print(F)
print(type(F))

# 7.0
F: int = 125
C: float = 5.0 * (F - 32.0)/9.0
print(C)
print(type(C))

# 8.0
K: int = 230
C: float = K - 273.15
print(C)
print(type(C))

# 9.0
C: int = 40
K: float = C + 273.15
print(K)
print(type(K))

# 10.0
K: int = 120
M: float = K/3.6
print(M)
print(type(M))

# 11.0
vel_metros_por_seg: int = int(input('Leia a velocidade em metros por segundo: '))
quilometros_conversao: float = vel_metros_por_seg * 3.6
print(quilometros_conversao)

# 12.0
milhas: int = int(input('Leia as milhas: '))
conversao_km: float = 1.61 * milhas
print(conversao_km)

# 13.0
km: int = int(input('Leia a velocidadade em Km: '))
milhas: float = km / 1.61
print(milhas)

# 18.0
volume: int = int(input('O volume em metros cúbicos é: '))
litros: float = volume * 1000
print(litros)

# 19.0
litros: int = int(input('Leia o volume em litros: '))
volume: float = litros / 1000
print(volume)

# 20.0
kg: int = int(input('Leia a massa em kg: '))
libras: float = kg / 0.45
print(f'A massa em kg {kg} convertida em libras é {libras}')

# 28.0
num1: int = int(input('Leia o primeiro valor: '))
num2: int = int(input('Leia o segundo valor: '))
num3: int = int(input('Leia o terceiro valor: '))
soma: int = num1 ** 2 + num2 ** 2 + num3 ** 2
print(soma)

# 29.0
n1: float = float(input('Digite a nota 1: '))
n2: float = float(input('Digite a nota 2: '))
n3: float = float(input('Digite a nota 3: '))
n4: float = float(input('Digite a nota 4: '))
media = (n1 + n2 + n3 + n4) / 4
print(f'A média é {media}')

# 30.0
dolar: float = 5.36
real: float = float(input('Leia o valor em real: '))
conversao: float = real * dolar
print(conversao)

# 31.0
num: int = int(input('Leia um número inteiro: '))
print(num + 1)
print(num - 1)

# 33.0
lado_quadrado: int = int(input('Leia o lado de um quadrado: '))
area: int = lado_quadrado ** 2
print(area)

# 34.0
raio: int = int(input('Leia o raio de uma circunferência: '))
pi: float = 3.14
area: float = pi * raio ** 2
print(area)

# 36.0
altura: int = int(input('Leia a altura do cilíndro: '))
raio: int = int(input('Leia o raio do cilíndro: '))
pi: float = 3.14
volume: float = pi * raio ** 2 * altura
print(volume)

# 37.0
valor: int = int(input('Leia o valor do produto: '))
desconto: float = valor * 0.12
valor_final: float = valor - desconto
print(valor_final)

# 38.0
salario: int = int(input('Leia o salário do funcionário: '))
aumento: float = salario * 0.25
novo_salario: float = salario + aumento
print(novo_salario)

# 50.0
ano: int = 2021
idade: int = int(input('Leia a idade: '))
ano_nascimento: int = ano - idade
print(ano_nascimento)
