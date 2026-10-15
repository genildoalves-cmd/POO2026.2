# Definindo exceções personalizadas
class SalarioInvalidoError(Exception):
    pass

class EmailInvalidoError(Exception):
    pass


# 6. Classe Funcionario(nome, salario)
class Funcionario:
    SALARIO_MINIMO = 1412.00  # Valor base para o salário mínimo

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario  # Chama o setter automaticamente

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self.SALARIO_MINIMO:
            raise SalarioInvalidoError(f"Salário (R$ {valor:.2f}) não pode ser inferior ao salário mínimo (R$ {self.SALARIO_MINIMO:.2f}).")
        self._salario = valor

    def aumentar(self, percentual):
        if not (0 < percentual <= 30):
            raise ValueError("O percentual de aumento deve ser maior que 0 e no máximo 30%.")
        self._salario += self._salario * (percentual / 100)


# 7. Classe Email(endereco)
class Email:
    def __init__(self, endereco):
        self.endereco = endereco  # Chama o setter automaticamente

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError("Endereço de e-mail inválido. Deve conter '@' e '.'.")
        self._endereco = valor


# 8. Testes dos dois casos de erro de cada classe com try/except
if __name__ == "__main__":
    print("=== TESTES DA CLASSE FUNCIONARIO ===")
    
    # Erro 1: Salário abaixo do mínimo
    try:
        f1 = Funcionario("João", 1000.0)
    except SalarioInvalidoError as e:
        print(f"Erro [Salário abaixo do mínimo]: {e}")

    # Erro 2: Aumento inválido (> 30% ou <= 0%)
    try:
        f2 = Funcionario("Maria", 3000.0)
        f2.aumentar(40)  # Tentativa de aumento superior a 30%
    except ValueError as e:
        print(f"Erro [Percentual de aumento inválido]: {e}")


    print("\n=== TESTES DA CLASSE EMAIL ===")

    # Erro 1: E-mail sem '@'
    try:
        e1 = Email("utilizador.com")
    except EmailInvalidoError as e:
        print(f"Erro [Falta '@']: {e}")

    # Erro 2: E-mail sem '.'
    try:
        e2 = Email("utilizador@com")
    except EmailInvalidoError as e:
        print(f"Erro [Falta '.']: {e}")