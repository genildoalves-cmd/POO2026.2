"""
O que este código faz:
1. Livro: Valida se o ano de publicação faz sentido (entre 0 e o ano atual) e se o número
   de páginas é maior que zero.
2. Biblioteca: Guarda os objetos Livro numa lista (self.acervo) e permite adicionar
   ou procurar livros.
3. Tratamento de Exceções: Se tentar criar um livro com dados inválidos ou procurar um
   livro que não está na lista, o programa lança e captura as exceções personalizadas (
   AnoInvalidoError, PaginasInvalidasError, LivroNaoEncontradoError) sem "crashar".
"""


# Definindo exceções personalizadas
class AnoInvalidoError(Exception):
    pass


class PaginasInvalidasError(Exception):
    pass


class LivroNaoEncontradoError(Exception):
    pass


# 1. Classe Livro(titulo, autor, ano, paginas)
# Valida se o ano de publicação faz sentido (entre 0 e o ano atual) e se o número de páginas é maior que zero.
class Livro:
    ANO_ATUAL = 2026  # Ano limite para cadastro de livros

    def __init__(self, titulo, autor, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano  # Chama o setter do ano automaticamente
        self.paginas = paginas  # Chama o setter de paginas automaticamente

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 0 or valor > self.ANO_ATUAL:
            raise AnoInvalidoError(
                f"Ano inválido ({valor}). Deve estar entre 0 e {self.ANO_ATUAL}."
            )
        self._ano = valor

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, valor):
        if valor <= 0:
            raise PaginasInvalidasError(
                f"Número de páginas inválido ({valor}). Deve ser maior que 0."
            )
        self._paginas = valor

    def __str__(self):
        return f"'{self.titulo}' - {self.autor} ({self.ano}) | {self.paginas} págs."


# 2. Classe Biblioteca
# Guarda os objetos Livro numa lista (self.acervo) e permite adicionar ou procurar livros.
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


# 3. Tratamento de Exceções
# Se tentar criar um livro com dados inválidos ou procurar um livro que não está na lista,
# o programa lança e captura as exceções personalizadas (AnoInvalidoError, PaginasInvalidasError, LivroNaoEncontradoError) sem "crashar".
if __name__ == "__main__":
    biblioteca = Biblioteca()

    print("=== TESTES DE VALIDAÇÃO DE LIVRO ===")

    # Erro 1: Ano de publicação inválido (ano futuro ou negativo)
    try:
        l1 = Livro("Dom Casmurro", "Machado de Assis", 2050, 250)
    except AnoInvalidoError as e:
        print(f"Erro [Ano inválido]: {e}")

    # Erro 2: Número de páginas inválido (<= 0)
    try:
        l2 = Livro("O Alquimista", "Paulo Coelho", 1988, -10)
    except PaginasInvalidasError as e:
        print(f"Erro [Páginas inválidas]: {e}")

    # Criando um livro válido para adicionar à biblioteca
    l3 = Livro("1984", "George Orwell", 1949, 328)
    biblioteca.adicionar_livro(l3)

    print("\n=== TESTES DE BUSCA NA BIBLIOTECA ===")

    # Erro 3: Buscar um livro que não existe na lista
    try:
        biblioteca.buscar_por_titulo("O Senhor dos Anéis")
    except LivroNaoEncontradoError as e:
        print(f"Erro [Livro não encontrado]: {e}")
