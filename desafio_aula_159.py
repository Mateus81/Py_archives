""" Type Hinting and annotations"""

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} " .center(50, '#')

print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))
print(cabecalho.__annotations__)
