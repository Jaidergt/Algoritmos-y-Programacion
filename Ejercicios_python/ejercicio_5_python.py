calificacion1 = float(input("Ingresa la primera calificación parcial: "))
calificacion2 = float(input("Ingresa la segunda calificación parcial: "))
calificacion3 = float(input("Ingresa la tercera calificación parcial: "))
examen_final = float(input("Ingresa la calificación del examen final: "))
trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3

calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("La calificación final del alumno es: ", calificacion_final)