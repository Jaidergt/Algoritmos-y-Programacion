Algoritmo ejercicio_12_promedio_materias
	Definir examenMatematicas, tarea1Matematicas, tarea2Matematicas, tarea3Matematicas Como Real
    Definir examenFisica, tarea1Fisica, tarea2Fisica Como Real
    Definir examenQuimica, tarea1Quimica, tarea2Quimica, tarea3Quimica Como Real
    Definir promedioMatematicas, promedioFisica, promedioQuimica, promedioGeneral Como Real
    

    Escribir "Ingrese la calificaci�n del examen de Matem�ticas:"
    Leer examenMatematicas
    Escribir "Ingrese las calificaciones de las 3 tareas de Matem�ticas:"
    Leer tarea1Mat, tarea2Matematicas, tarea3Matematicas
    
    
    Escribir "Ingrese la calificaci�n del examen de F�sica:"
    Leer examenFisica
    Escribir "Ingrese las calificaciones de las 2 tareas de F�sica:"
    Leer tarea1Fis, tarea2Fisica
    
    
    Escribir "Ingrese la calificaci�n del examen de Qu�mica:"
    Leer examenQuimica
    Escribir "Ingrese las calificaciones de las 3 tareas de Qu�mica:"
    Leer tarea1Quimica, tarea2Quimica, tarea3Quimica
    
    
    promedioMat <- (examenMatematicas * 0.90) + ((tarea1Matematicas + tarea2Matematicas + tarea3Matematicas) / 3 * 0.10)
    promedioFis <- (examenFisica * 0.80) + ((tarea1Fisica + tarea2Fisica) / 2 * 0.20)
    promedioQui <- (examenQuimica* 0.85) + ((tarea1Quimica + tarea2Quimica + tarea3Quimica) / 3 * 0.15)
    
    promedioGeneral <- (promedioMatematicas + promedioFisica + promedioQuimica) / 3
    
    Escribir "-------------------------------------------"
    Escribir "Promedio en Matem�ticas: ", promedioMatematicas
    Escribir "Promedio en F�sica: ", promedioFisica
    Escribir "Promedio en Qu�mica: ", promedioQuimica
    Escribir "-------------------------------------------"
    Escribir "Promedio General: ", promedioGeneral
FinAlgoritmo
