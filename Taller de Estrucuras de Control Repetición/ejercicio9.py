n = int(input("Ingrese la cantidad de estudiantes: "))
puntajes = []

for _ in range(n):
    nombre = input("Nombre del estudiante: ")
    puntaje = float(input("Puntaje: "))
    puntajes.append((nombre, puntaje))

puntajes.sort(key=lambda x: x[1])
mejor = puntajes[-1]
peor = puntajes[0]

promedio = sum(p[1] for p in puntajes) / n
menores_al_promedio = sum(1 for p in puntajes if p[1] < promedio)
mayores_al_promedio = sum(1 for p in puntajes if p[1] > promedio)

print("Mejor puntaje:", mejor[0], mejor[1])
print("Peor puntaje:", peor[0], peor[1])
print("Promedio:", promedio)
print("Porcentaje de estudiantes debajo del promedio:", (menores_al_promedio / n) * 100, "%")
print("Porcentaje de estudiantes arriba del promedio:", (mayores_al_promedio / n) * 100, "%")