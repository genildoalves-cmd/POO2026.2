# distribuidor 28 % d
d = 28
# imposto i 45 %
i = 45 

# custo de fabrica c

c = float(input("custo de fabrica: "))

t = c + (i / 100 * c) + (c * d / 100)
print(f"o custo ao consumidor é: {t:.3f}")
