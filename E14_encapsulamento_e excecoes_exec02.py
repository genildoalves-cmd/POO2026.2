import sys

# =====================================================================
# 1. EXCEÇÕES DA CONTA (Devem vir primeiro para o Python conhecê-las)
# =====================================================================
class ErroDeConta(Exception):
    """Classe base para todos os erros da conta bancária."""
    pass

class ValorInvalidoError(ErroDeConta):
    pass

class SaldoInsuficienteError(ErroDeConta):
    pass

class LimiteExcedidoError(ErroDeConta):
    pass


# =====================================================================
# 2. CLASSE DA CONTA BANCÁRIA
# =====================================================================
class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do depósito deve ser maior que zero."
            )
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do saque deve ser maior que zero."
            )

        if valor > 1000:
            raise LimiteExcedidoError(
                "O limite de saque por operação é R$ 1.000."
            )

        if valor > self._saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente."
            )

        self._saldo -= valor


# =====================================================================
# 3. FUNÇÃO DE TESTES AUTOMATIZADOS (Para verificar se os erros funcionam)
# =====================================================================
def executar_testes_automatizados():
    print("\n--- INICIANDO TESTES DOS ERROS ---")
    c = ContaBancaria()
    
    # Teste 1: Depósito inválido
    try:
        c.depositar(-10)
        print("❌ Teste 1 falhou: Aceitou depósito negativo.")
    except ValorInvalidoError as e:
        print(f"✅ Teste 1 passou (ValorInvalidoError): {e}")

    # Teste 2: Limite de Saque Excedido
    try:
        c.depositar(2000)
        c.sacar(1500)
        print("❌ Teste 2 falhou: Aceitou saque acima de R$ 1000.")
    except LimiteExcedidoError as e:
        print(f"✅ Teste 2 passou (LimiteExcedidoError): {e}")

    # Teste 3: Saldo Insuficiente
    try:
        conta_limpa = ContaBancaria()
        conta_limpa.sacar(50)
        print("❌ Teste 3 falhou: Aceitou saque sem ter saldo.")
    except SaldoInsuficienteError as e:
        print(f"✅ Teste 3 passou (SaldoInsuficienteError): {e}")
        
    print("-----------------------------------\n")


# =====================================================================
# 4. PROGRAMA PRINCIPAL (CAIXA ELETRÔNICO)
# =====================================================================
conta = ContaBancaria()

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Executar Testes de Erro")
    print("5 - Sair")

    try:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
            print("Depósito realizado com sucesso.")

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
            print("Saque realizado com sucesso.")

        elif opcao == "3":
            print(f"Saldo: R$ {conta.saldo:.2f}")

        elif opcao == "4":
            executar_testes_automatizados()

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Digite um número válido (apenas algarismos).")

    except ErroDeConta as erro:
        print(f"\n⚠️  Erro detectado: {erro}")
