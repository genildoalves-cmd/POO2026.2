vb = int(input("votos brancos:"))
vn = int(input("votos nulos:"))
vv = int(input("votos validos:"))

vt = vb + vn + vv
print("total de votos", vt)
pct_vb = (vb * 100) / vt
pct_vn = (vn * 100) / vt
pct_vv = (vv * 100) / vt
print(f"percentual de votos brancos:{pct_vb:.2f}%")
print(f"percentual de votos nulos:{pct_vn:.2f}%")
print(f"percentual de votos validos:{pct_vv:.2f}%")
