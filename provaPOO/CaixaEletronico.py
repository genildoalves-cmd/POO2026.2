from ContaBancaria import ContaBancaria
from Excecoes import ValorInvalido, LimiteExcedido, SaldoInsuficiente

c1 = ContaBancaria()

    
while True:    
    print("\n ===== CAIXA ELETRÔNICO ======")
    print("\n === 1 - DEPOSITO ==")
    print("\n === 2 - SACAR ==")
    print("\n === 3 - SALDO ==")
    print("\n === 4 - TESTE ==")
    print("\n === 5 - SAIR ==")
    
    try:
        opcao = int(input("\n Informe numero : "))
        if opcao < 1 or opcao > 5:
         print("Opção inválida! Escolha um número entre 1 e 5.")
    except ValueError:
        print("Por favor, informe um número válido.")
    if opcao == 1:
        print("valor do deposito:")
        valor = float(input("valor do deposito: "))
        c1.depositar(valor)
        print("Deposito Realizado")
    elif opcao == 2:
        print("sair")
        break
        
  
    
    
        