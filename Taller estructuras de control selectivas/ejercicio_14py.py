lectura_anterior = float(input("Ingrese la lectura anterior: "))
lectura_actual = float(input("Ingrese la lectura actual: "))
consumo = lectura_actual - lectura_anterior
if consumo <= 100:
    costo = consumo * 4600
elif consumo <= 300:
    costo = consumo * 8000
elif consumo <= 500:
    costo = consumo * 100000
else:
    costo = consumo * 120000
print(f"Monto a pagar: {costo}")
