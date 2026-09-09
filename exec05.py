import math

c = float(input("informe o comprimento:"))
l = float(input("informe a largura:"))

t = l * c
p_lampada = t * 18

print("Total de lampadas:", math.ceil(p_lampada / 60))
