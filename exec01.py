v1 = int(input("Informe o valor inteiro 1: "))
v2 = int(input("Informe o valor inteiro 2: "))
v3 = int(input("Informe o valor inteiro 3: "))


if v3 > v1 and v3 < v2:
    print(f"o valor {v3} esta entre {v1} e {v2}")
elif v3 < v1:
    print(f"o valor de {v3} é menor que {v1}")
elif v3 >v2:
    print(f"o valor de {v3} é maior que {v2}")
else:
    print(f"o valor de {v3} é igual a {v1} ou {v2}")
    