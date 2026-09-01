# 1. Entrada de dados: leitura das 4 notas digitadas pelo usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# 2. Processamento: cálculo da média aritmética das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# 3. Saída de dados: exibição das notas digitadas e da média final
print(f"\nNotas digitadas: {nota1}, {nota2}, {nota3} e {nota4}")
print(f"Média aritmética: {media:.2f}")
    