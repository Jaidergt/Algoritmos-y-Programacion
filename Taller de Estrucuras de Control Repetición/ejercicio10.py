num = int(input("Ingrese un número: "))
suma = sum(i for i in range(1, num) if num % i == 0)

if suma == num:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")