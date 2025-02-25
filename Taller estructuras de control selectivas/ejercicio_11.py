temp = float(input("Ingrese la temperatura: "))
if temp > 85:
    deporte = "Natación"
elif temp > 70:
    deporte = "Tenis"
elif temp > 32:
    deporte = "Golf"
elif temp > 10:
    deporte = "Esquí"
else:
    deporte = "Marcha"
print(f"Deporte recomendado: {deporte}")