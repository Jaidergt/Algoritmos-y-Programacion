def calcular_promedio_materia(nombre_materia, examen, tareas, peso_examen, peso_tareas):
    promedio_tareas = sum(tareas) / len(tareas)  # Promedio de tareas
    promedio_final = (examen * peso_examen) + (promedio_tareas * peso_tareas)
    return promedio_final

# Solicitar calificaciones para Matemática
print("Ingrese las calificaciones de Matemática:")
examen_matematica = float(input("Nota del examen: "))
tareas_matematica = [float(input(f"Nota de la tarea {i+1}: ")) for i in range(3)]
promedio_matematica = calcular_promedio_materia("Matemática", examen_matematica, tareas_matematica, 0.90, 0.10)

# Solicitar calificaciones para Física
print("\nIngrese las calificaciones de Física:")
examen_fisica = float(input("Nota del examen: "))
tareas_fisica = [float(input(f"Nota de la tarea {i+1}: ")) for i in range(2)]
promedio_fisica = calcular_promedio_materia("Física", examen_fisica, tareas_fisica, 0.80, 0.20)

# Solicitar calificaciones para Química
print("\nIngrese las calificaciones de Química:")
examen_quimica = float(input("Nota del examen: "))
tareas_quimica = [float(input(f"Nota de la tarea {i+1}: ")) for i in range(3)]
promedio_quimica = calcular_promedio_materia("Química", examen_quimica, tareas_quimica, 0.85, 0.15)

# Calcular el promedio general
promedio_general = (promedio_matematica + promedio_fisica + promedio_quimica) / 3

# Mostrar resultados
print("\n--- PROMEDIOS FINALES ---")
print(f"Promedio en Matemática: {promedio_matematica:.2f}")
print(f"Promedio en Física: {promedio_fisica:.2f}")
print(f"Promedio en Química: {promedio_quimica:.2f}")
print(f"\nPromedio general: {promedio_general:.2f}")