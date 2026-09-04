a = int(input("informe valor de a: "))
b = int(input("informe valor de b: "))
c = int(input("informe valor de c: "))
if a < b < c:
    print(f"crescente:{a},{b},{c}")
    
elif a < c < b:
    
    print(f"crescente::{a},{c},{b}")
    
elif b < c < a:
    
    print(f"crescente::{b},{c},{a}")
    
elif b < a < c:
    
    print(f"crescente::{b},{a},{c}")

elif c < a < b:
    
    print(f"crescente::{c},{a},{b}")
    
elif c < b < a:
    
    print(f"crescente::{c},{b},{a}")
else:
    print(f"valores iguais")