# 1. Solicita os 3 valores inteiros

    a = int(input("Digite o 1º número inteiro: "))
    b = int(input("Digite o 2º número inteiro: "))
    c = int(input("Digite o 3º número inteiro: "))

# 2. Pergunta ao usuário a ordem desejada

    print("\nEscolha a ordem de exibição:")
    print("1 - Crescente")
    print("2 - Decrescente")
    opcao = int(input("Digite a opção (1 ou 2): "))

# 3. Lógica de ordenação usando IF / ELSE
# Descobrindo a ordem crescente (menor, meio, maior)

    if a <= b and a <= c:
        menor = a
        if b <= c:
            meio = b
            maior = c
        else:
            meio = c
            maior = b
    elif b <= a and b <= c:
        menor = b
        if a <= c:
            meio = a
            maior = c
        else:
            meio = c
            maior = a
    else:
        menor = c
        if a <= b:
            meio = a
            maior = b
        else:
            meio = b
            maior = a

    # 4. Exibição com base na escolha do usuário
    
    if opcao == 1:
        print(f"\nValores em ordem crescente: {menor}, {meio}, {maior}")
    elif opcao == 2:
        print(f"\nValores em ordem decrescente: {maior}, {meio}, {menor}")
    else:
        print("\nOpção inválida!")
