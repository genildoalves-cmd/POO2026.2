"""
Sistema de Clínica Médica
1. Paciente: Valida a idade (deve ser entre 0 e 120 anos) e a altura (deve ser maior que zero).
2. Clinica: Guarda os pacientes num dicionário (self.pacientes) utilizando o CPF como chave.
3. Tratamento de Exceções: Lança IdadeInvalidaError, AlturaInvalidaError e PacienteNaoEncontradoError.
"""


# Exceções personalizadas
class IdadeInvalidaError(Exception):
    pass


class AlturaInvalidaError(Exception):
    pass


class PacienteNaoEncontradoError(Exception):
    pass


# 1. Classe Paciente(cpf, nome, idade, altura)
class Paciente:
    def __init__(self, cpf, nome, idade, altura):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade  # Chama o setter de idade
        self.altura = altura  # Chama o setter de altura

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0 or valor > 120:
            raise IdadeInvalidaError(
                f"Idade inválida ({valor}). Deve estar entre 0 e 120 anos."
            )
        self._idade = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise AlturaInvalidaError(
                f"Altura inválida ({valor}). Deve ser maior que 0 metros."
            )
        self._altura = valor

    def __str__(self):
        return f"CPF: {self.cpf} | Nome: {self.nome} | Idade: {self.idade} anos | Altura: {self.altura}m"


# 2. Classe Clinica (Utilizando Dicionário)
class Clinica:
    def __init__(self):
        # Dicionário: { 'cpf_do_paciente': objeto_Paciente }
        self.pacientes = {}

    def cadastrar_paciente(self, paciente):
        self.pacientes[paciente.cpf] = paciente
        print(f"Paciente '{paciente.nome}' cadastrado com sucesso!")

    def buscar_por_cpf(self, cpf):
        # Busca direta pela chave do dicionário
        if cpf in self.pacientes:
            return self.pacientes[cpf]
        raise PacienteNaoEncontradoError(f"Nenhum paciente cadastrado com o CPF: {cpf}")


# 3. Testes com try/except
if __name__ == "__main__":
    clinica = Clinica()

    print("=== TESTES DE VALIDAÇÃO DE PACIENTE ===")

    # Erro 1: Idade inválida
    try:
        p1 = Paciente("111.222.333-44", "Carlos", -5, 1.75)
    except IdadeInvalidaError as e:
        print(f"Erro [Idade inválida]: {e}")

    # Erro 2: Altura inválida
    try:
        p2 = Paciente("222.333.444-55", "Ana", 30, 0.0)
    except AlturaInvalidaError as e:
        print(f"Erro [Altura inválida]: {e}")

    # Cadastrando um paciente válido no dicionário
    p_valido = Paciente("123.456.789-00", "Maria Silva", 28, 1.65)
    clinica.cadastrar_paciente(p_valido)

    print("\n=== TESTES DE BUSCA NO DICIONÁRIO ===")

    # Busca bem-sucedida pelo CPF
    try:
        resultado = clinica.buscar_por_cpf("123.456.789-00")
        print(f"Paciente encontrado: {resultado}")
    except PacienteNaoEncontradoError as e:
        print(f"Erro: {e}")

    # Erro 3: CPF não cadastrado
    try:
        clinica.buscar_por_cpf("000.000.000-00")
    except PacienteNaoEncontradoError as e:
        print(f"Erro [Paciente não encontrado]: {e}")
