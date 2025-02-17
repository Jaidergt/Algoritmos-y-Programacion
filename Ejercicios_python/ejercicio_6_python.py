total_estudiantes = int(input("Ingresa el número total de estudiantes en el grupo: "))
numero_hombres = int(input("Ingresa el número de hombres en el grupo: "))
numero_mujeres = total_estudiantes - numero_hombres  

porcentaje_hombres = (numero_hombres / total_estudiantes) * 100
porcentaje_mujeres = (numero_mujeres / total_estudiantes) * 100

print(f"El porcentaje de hombres es: {porcentaje_hombres:.2f}%")
print(f"El porcentaje de mujeres es: {porcentaje_mujeres:.2f}%")