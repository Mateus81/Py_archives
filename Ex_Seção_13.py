"""
Exercícios
"""

import string
from datetime import date

# 1.0
arquivo = open("arq.txt")
print(arquivo.read())
arquivo.close()

# 2.0
arquivo = open("arq.txt")
print(len(arquivo.readlines()))
arquivo.close()

# 3.0
numero_vogais = 0
arquivo = open("arq.txt")
for n in arquivo.read():
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        numero_vogais += 1
print(numero_vogais)

# 4.0
numero_vogais = 0
numero_consoantes = 0
with open("arq.txt") as arquivo:
    for n in arquivo.read():
        if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
            numero_vogais += 1
        if n == 'b' or n == 'c' or n == 'd' or n == 'f' or n == 'g' or n == 'h':
            numero_consoantes += 1
print(numero_vogais)
print(numero_consoantes)


# 5.0 (copiado e colado)
def busca(arq, caractere):
    try:
        with open(arq, 'r+', encoding='UTF-8') as arquivo_atual:
            caracteres = []
            for i in arquivo_atual.read():
                if caractere == i:
                    caracteres.append(caractere)
        return f'O caractere {caractere} aparece em {arquivo_atual.name} {len(caracteres)} vezes.'
    except FileNotFoundError:
        return 'Arquivo não encontrado.'


a = input('Arquivo: ')
c = input('Caractere a ser buscado: ')

print(busca(a, c))

# 6.0
contagem = 0
consoante = 0
alfabeto = string.ascii_uppercase

a = input('Digite o arquivo: ')
with open(a, 'r') as arquivo_atual:
    lista = arquivo_atual.read()

[[print(f'a letra {caracter} aparece {lista.upper().count(caracter)} vezes') for caracter in letras] for
 letras in alfabeto]

# 7.0
with open("novo.txt", "w") as arquivo:
    arquivo.write('*bcd* 0\n')
    arquivo.write('fgh*')

# 8.0
file1: str = input('Leia o primeiro arquivo: ')
file2: str = input('Leia o segundo arquivo: ')
with open(file1, encoding='UTF-8') as arq:
    texto = arq.read()
with open(file2, "w", encoding='UTF-8') as arq:
    arq.write(texto.upper())

# 9.0
arquivo1 = "arq.txt"
arquivo2 = "novo.txt"
arquivo3 = arquivo1 + arquivo2
with open("uniao.txt", "w") as arq3:
    arq3.write('abcde 0\n')
    arq3.write('fghi\n')
    arq3.write('*bcd* 0\n')
    arq3.write('fgh*\n')

# 12.0
nome_arquivo: str = input('Leia o nome do arquivo. formato nome.extensao: ')
dicionario: dict = dict()
with open(f'{nome_arquivo}', 'r', encoding='UTF-8') as arquivo:
    caracter = str(arquivo.read())
    arquivo.seek(0)
    palavra = arquivo.read().split()
    arquivo.seek(0)
    print(f'A quantidade de caracteres: {len(caracter)}')
    print(f'A quantidade de linhas: {len(arquivo.readlines())}')
    print(f'A quantidade de palavras: {len(palavra)}')
    print(f'A quantidade de cada letra do alfabeto no texto(caracteres acentuados serão ignorados): ')
    [dicionario.update({letra: caracter.lower().count(letra)}) for letra in caracter.lower()
     if letra in string.ascii_letters]
    for key, value in sorted(dicionario.items()):
        print(f'{key} - {value}')

# 14.0
arquivo = input('Leia o nome do arquivo: ')
with open(arquivo, encoding='UTF-8') as file:
    arq_novo = open('quantos_anos.txt', 'w', encoding='UTF-8')
    for linha in file.readlines():
        linha = linha.strip('\n')
        datas = linha.split()

        inicio = date(int(datas[4]), int(datas[3]), int(datas[2]))
        final = date.today()
        data_final = final - inicio
        ano = data_final.days

        arq_novo.write(f'{datas[0]} tem {ano} anos')
        arq_novo.write('\n')

# 16.0
vetor = [3, 7, 5, 4, 1, 2, 9, 6, 5, 7]
with open("binario.txt", "w") as binario:
    for n in vetor:
        binario.write(f'{bin(n)}\n')

# 18.0
soma: int = (5 + 7 + 25 + 2)
with open("produtos.txt", "w") as lista_produtos:
    lista_produtos.write('arroz: 5.00 reais\n')
    lista_produtos.write('feijao: 7.00 reais \n')
    lista_produtos.write('alcatra: 25.00 reais\n')
    lista_produtos.write('abacaxi: 2.00 reais\n')

print(f'{soma} reais')

# 23.0
with open("emp.txt", "w") as arquivo:
    arquivo.write('funcionario 1: Zelador, 1 ano\n')
    arquivo.write('funcionario 2: Porteiro, 2 anos\n')
    arquivo.write('funcionario 3: Assistente , 1 ano\n')
    arquivo.write('funcionario 4: Chefe financeiro, 4 anos\n')
    arquivo.write('funcionario 5: CEO, 5 anos anos\n')
