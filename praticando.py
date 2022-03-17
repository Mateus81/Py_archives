caracteres: str = "Testando slicing"
s1 = caracteres[0:9]
print(s1)  # Slice separa por dois índices indicados
print(caracteres)
print(caracteres.split()[1])  # Split separa a palavra inteira pelo índice

varnum: str = "6.4"
print(type(varnum))
converte = float(varnum)
print(converte + 12)

a: str = "22.3"
b = float(a)
print(b)

c = int(b)
print(c)
