"""04. Faça um programa que recebe o nome completo de um funcionário, o número de horas
trabalhadas por mês, o valor que recebe por hora trabalhada e o número de filhos. Com estas
informações, o programa deve calcular o salário deste funcionário, sabendo que para cada
filho, o funcionário recebe 3% a mais, calculado sobre o salário bruto."""

nome = input("informe nome do funcionario:")
hs = input ("horas trabalhadas por mes:")
v = input ("valor que recebe por horas")
filhos = input("numeros de filhos por funcionario:")

# Convertendo as entradas para números
hs = int(hs)
v = float(v)
filhos = int(filhos)

# Calculando o salário bruto
salario_bruto = hs * v

# Calculando o bônus por filhos
bonus_filhos = salario_bruto * 0.03 * filhos

# Calculando o salário final
salario_final = salario_bruto + bonus_filhos

# Exibindo o resultado
print(f"Nome do funcionário: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Bonus por filhos: R$ {bonus_filhos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")