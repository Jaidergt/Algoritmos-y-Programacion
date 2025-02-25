cantidad = float(input("Ingrese la cantidad en inversión: "))
interes = cantidad * 0.05  # Suponiendo un 5% de interés
if interes > 100000:
    cantidad += interes
print(f"Total en la cuenta: {cantidad}")