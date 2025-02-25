sueldo = float(input("Ingrese el sueldo: "))
aumento = 0.15 if sueldo < 900000 else 0.12
nuevo_sueldo = sueldo * (1 + aumento)
print(f"Nuevo sueldo: {nuevo_sueldo}")
