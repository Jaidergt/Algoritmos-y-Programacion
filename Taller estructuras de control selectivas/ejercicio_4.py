monto = float(input("Ingrese el monto de la compra: "))
if monto > 5000000:
    inversion = monto * 0.55
    prestamo = monto * 0.30
    credito = monto * 0.15
else:
    inversion = monto * 0.70
    credito = monto * 0.30
    prestamo = 0
intereses = credito * 0.20
print(f"Inversión: {inversion}, Préstamo: {prestamo}, Crédito: {credito}, Intereses: {intereses}")