valores = []
contador = 0
contador2 = 0

for i in range(6):
    n = float(input(""))
    if n > 0:
        contador += 1
        valores.append(n)
    else:
        contador2 += 1
    
promedio = sum(valores) / contador

print(f"{contador} valores positivos")
print(f"{promedio:.1f}")