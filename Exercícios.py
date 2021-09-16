"""
Exercícios
"""
import math
# 1.0
numero1: int = int(input('Digite seu primeiro número: '))
numero2: int = int(input('Digite seu segundo número: '))
if numero1 > numero2:
    print(f'Seu primeiro número: {numero1} é maior que o segundo.')
else:
    print(f'Seu segundo número: {numero2} é maior que o primeiro')
# 2.0
num: int = 9
if num >= 0:
    print(f'A raiz quadrada de {num} é {math.sqrt(num)}')
else:
    print('O número é inválido.')

# 3.0
num: float = -9.0
if num >= 0:
    print(f'A raiz quadrada de {num} é {math.sqrt(num)}')
else:
    print(9 * 9)
    print(type(9 ** 2))

# 4.0
num: int = 4
if num >= 0:
    print(4 ** 2)
    print(4 // 2)

# 5.0
num: int = 8
valor = num & 2
if valor == 0:
    print('Este número é par')
else:
    print('Este número é impar')

# 6.0
num1: int = 8
num2: int = 2
print(f'A diferença entre eles é {num1 - num2}')
if num1 > num2:
    print('O número1 é maior que o número2')
else:
    print('O número2 é maior que o número1')

# 7.0
num1: int = 6
num2: int = 6
if num1 > num2:
    print('O número1 é maior que o número2')
elif num1 == num2:
    print('Ambos são iguais')
else:
    print('O número 2 é maior que o número 1')

# 8.0
nota1: int = 8
nota2: int = 5
if nota1 >= 7:
    print('Nota válida')
    if nota2 <= 7:
        print('Nota inválida')

# 9.0
salario: int = 2500
emprestimo: int = 4000
saip = (20 * salario) / 100
if emprestimo > saip:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')

# 10.0
h: float = 1.75
homens: float = (72.7 * h) - 58
print(homens)
mulheres: float = (62.1 * h) - 44.7
print(mulheres)

# 11.0
num: int = 350
print(3 + 5 + 0)
if num < 0:
    print('Número inválido')

# 12.0
num: int = int(input('Leia um número inteiro: '))
if num < 0:
    print('Número invalido')
else:
    print(math.log(num, 10))

# 15.0
num: int = int(input('Digite um número entre 1 e 7: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-feira')
elif num == 3:
    print('Terça-feira')
elif num == 4:
    print('Quarta-feira')
elif num == 5:
    print('Quinta-feira')
elif num == 6:
    print('Sexta-feira')
elif num == 7:
    print('Sábado')
else:
    print('Número inválido')

# 16.0
num: int = int(input('Digite um número entre 1 e 12: '))
if num == 1:
    print('Janeiro')
elif num == 2:
    print('Fevereiro')
elif num == 3:
    print('Março')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Maio')
elif num == 6:
    print('Junho')
elif num == 7:
    print('Julho')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Setembro')
elif num == 10:
    print('Outubro')
elif num == 11:
    print('Novembro')
elif num == 12:
    print('Dezembro')
else:
    print('Número inválido')

# 17.0
bmaior: float = float(input('Digite a base maior: '))
bmenor: float = float(input('Digite a base menor: '))
h: float = float(input('Digite a altura: '))
area: float = (bmaior + bmenor) * h / 2
print(area)

# 18.0
num1: int = int(input('Informe o primeiro número: '))
num2: int = int(input('Informe o segundo número: '))
opcao: int = int(input('Informe a opcão de 1 e 4: '))
if opcao == 1:
    print(num1 + num2)
elif opcao == 2:
    print(num1 - num2)
elif opcao == 3:
    print(num1 * num2)
elif opcao == 4:
    print(num1 / num2)
else:
    print('Opção inválida')

# 19.0
num: int = int(input('Informe o número: '))
if num % 3 == 0:
    print(f'{num} é divisível por 3')
elif num % 5 == 0:
    print(f'{num} é divisível por 5')
else:
    print('Número negado.')

# 23.0
ano: int = int(input('Leia o ano: '))
if ano % 400 == 0 and ano % 4 == 0 and not ano % 100 == 0:
    print(f'O ano {ano} é bissexto')

# 27.0
idade: int = (int(input('Digite a idade: ')))
if idade <= 7:
    print('Infantil A')
elif idade <= 11:
    print('Infantil B')
elif idade <= 14:
    print('Juvenil A')
elif idade <= 17:
    print('Juvenil B')
elif idade > 18:
    print('Senior')

# 30.0
n1: int = int(input('Leia o primeiro número: '))
n2: int = int(input('Leia o segundo número: '))
n3: int = int(input('Leia o terceiro número: '))
lista: list = [n1, n2, n3]
print(sorted(lista))
