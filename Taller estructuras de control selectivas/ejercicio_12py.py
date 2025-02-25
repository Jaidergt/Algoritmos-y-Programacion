cantidad = int(input("Ingrese una cantidad en COP: "))
billetes = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
monedas = [500, 200, 100, 50]
for b in billetes:
    if cantidad >= b:
        print(f"{cantidad // b} billetes de {b} COP")
        cantidad %= b
for m in monedas:
    if cantidad >= m:
        print(f"{cantidad // m} monedas de {m} COP")
        cantidad %= m
