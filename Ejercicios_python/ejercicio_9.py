def calcular_salario_neto(horas_trabajadas, precio_por_hora):
    # Calcular el sueldo base
    sueldo_base = horas_trabajadas * precio_por_hora
    # Aplicar el descuento del 20% por impuestos
    descuento = sueldo_base * 0.20
    salario_neto = sueldo_base - descuento
    return sueldo_base, descuento, salario_neto

# Solicitar datos al usuario
horas = float(input("Ingrese el número de horas trabajadas: "))
precio = float(input("Ingrese el precio por hora: "))

# Calcular el salario
sueldo_base, descuento, salario_neto = calcular_salario_neto(horas, precio)

# Mostrar resultados
print(f"\nSueldo base: ${sueldo_base:.2f}")
print(f"Descuento por impuestos (20%): ${descuento:.2f}")
print(f"Salario neto: ${salario_neto:.2f}")