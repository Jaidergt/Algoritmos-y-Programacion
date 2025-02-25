categoria = int(input("Ingrese la categoría: "))
sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
aumentos = {1: 0.10, 2: 0.15, 3: 0.20, 4: 0.40, 5: 0.60}
nuevo_sueldo = sueldo_bruto * (1 + aumentos.get(categoria, 0))
print(f"Categoría: {categoria}, Nuevo sueldo: {nuevo_sueldo}")