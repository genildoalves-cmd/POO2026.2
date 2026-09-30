"""
Sistema de Biblioteca
1. Livro: Usa get_ano(), set_ano(), get_paginas() e set_paginas() para validação.
2. Biblioteca: Guarda os objetos Livro numa lista (self.acervo).
3. Tratamento de Exceções: Captura AnoInvalidoError, PaginasInvalidasError e LivroNaoEncontradoError.
"""


# Definindo exceções personalizadas
class AnoInvalidoError(Exception):
    pass


class PaginasInvalidasError(Exception):
    pass


class LivroNaoEncontradoError(Exception):
    pass


# 1. Classe Livro(titulo, autor, ano, paginas)
class Livro:
    ANO_ATUAL = 2026

    def __init__(self, titulo, autor, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        # Usa os setters no construtor para aplicar as validações na criação
        self.set_ano(ano)
        self.set_paginas(paginas)

    # Getters e Setters para 'ano'
    def get_ano(self):
        return self._ano

    def set_ano(self, valor):
        if valor < 0 or valor > self.ANO_ATUAL:
            raise AnoInvalidoError(
                f"Ano inválido ({valor}). Deve estar entre 0 e {self.ANO_ATUAL}."
            )
        self._ano = valor

    # Getters e Setters para 'paginas'
    def get_paginas(self):
        return self._paginas

    def set_paginas(self, valor):
        if valor <= 0:
            raise PaginasInvalidasError(
                f"Número de páginas inválido ({valor}). Deve ser maior que 0."
            )
        self._paginas = valor

    def __str__(self):
        return f"'{self.titulo}' - {self.autor} ({self.get_ano()}) | {self.get_paginas()} págs."


# 2. Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.acervo = []  # Lista que armazena os livros

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def buscar_por_titulo(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        raise LivroNaoEncontradoError(
            f"O livro '{titulo}' não foi encontrado na biblioteca."
        )


# 3. Testes com try/except
if __name__ == "__main__":
    biblioteca = Biblioteca()

    print("=== TESTES DE VALIDAÇÃO DE LIVRO ===")

    # Erro 1: Ano de publicação inválido
    try:
        l1 = Livro("Dom Casmurro", "Machado de Assis", 2050, 250)
    except AnoInvalidoError as e:
        print(f"Erro [Ano inválido]: {e}")

    # Erro 2: Número de páginas inválido
    try:
        l2 = Livro("O Alquimista", "Paulo Coelho", 1988, -10)
    except PaginasInvalidasError as e:
        print(f"Erro [Páginas inválidas]: {e}")

    # Criando um livro válido
    l3 = Livro("1984", "George Orwell", 1949, 328)
    biblioteca.adicionar_livro(l3)

    print("\n=== TESTES DE BUSCA NA BIBLIOTECA ===")

    # Erro 3: Buscar livro inexistente
    try:
        biblioteca.buscar_por_titulo("O Senhor dos Anéis")
    except LivroNaoEncontradoError as e:
        print(f"Erro [Livro não encontrado]: {e}")
