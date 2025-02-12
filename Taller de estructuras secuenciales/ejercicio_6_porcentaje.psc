Algoritmo  ejercicio_6_porcentaje
	Escribir 	"Escribe la cantidad de hombres que hay en el grupo de estudiantes"
	leer h
	Escribir 	"Escribe la cantidad de mujeres que hay en el grupo de estudiantes"
	leer m
    testudiantes <- h + m  
    phombres <- (h / testudiantes) * 100
    pmujeres <- (m / testudiantes) * 100
    Escribir "Porcentaje de hombres en el grupo de estudiantes es : ", phombres, " %"
    Escribir "Porcentaje de mujeres en el grupo de estudiantes es : ", pmujeres, " %"
FinAlgoritmo
