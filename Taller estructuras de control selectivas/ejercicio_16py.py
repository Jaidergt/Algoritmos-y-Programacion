import math
A = float(input("Ingrese A: "))
B = float(input("Ingrese B: "))
C = float(input("Ingrese C: "))
D = B**2 - 4*A*C
if D > 0:
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print(f"Soluciones: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -B / (2*A)
    print(f"Solución única: x = {x}")
else:
    print("No tiene solución real")