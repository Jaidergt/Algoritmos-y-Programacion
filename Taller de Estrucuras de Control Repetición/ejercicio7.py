n = int(input("Ingrese el número de estudiantes: "))
max_altura = 0

for i in range(n):
    altura = float(input(f"Ingrese la altura del estudiante {i+1}: "))
    if altura > max_altura:
        max_altura = altura

print("La mayor altura es:", max_altura)