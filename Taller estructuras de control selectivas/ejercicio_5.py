ventas1 = float(input("Ingrese ventas del depto 1: "))
ventas2 = float(input("Ingrese ventas del depto 2: "))
ventas3 = float(input("Ingrese ventas del depto 3: "))
ventas_totales = ventas1 + ventas2 + ventas3
extra = 0.20
if ventas1 > ventas_totales * 0.33:
    print("Depto 1 recibe incentivo")
if ventas2 > ventas_totales * 0.33:
    print("Depto 2 recibe incentivo")
if ventas3 > ventas_totales * 0.33:
    print("Depto 3 recibe incentivo")

# Ejercicio 6: Redondeo a la centena más cercana
N = int(input("Ingrese un número de 4 dígitos: "))
redondeado = round(N, -2)
print(f"Número redondeado: {redondeado}")
