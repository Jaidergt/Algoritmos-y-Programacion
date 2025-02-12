Algoritmo ejercicio_5_calificacion_final
	Escribir 	"por favor coloque la calificacion del primer parcial"
	leer par1
	Escribir 	"por favor coloque la calificacion del segundo parcial"
	leer par2
	Escribir 	"por favor coloque la calificacion del tercer parcial"
	leer par3
	Escribir 	"por favor coloque la calificacion del examen final"
	leer exfinal
	Escribir 	"por favor coloque la calificacion del trabajo final"
	leer trafinal
    
    promedioPar <- (par1 + par2 + par3) / 3
    nfinal <- (promedioPar * 0.55) + (exfinal * 0.30) + (trafinal * 0.15)
    Escribir "El promedio de parciales es: ", promedioPar
    Escribir "La calificación final en computación es: ", nfinal
FinAlgoritmo
