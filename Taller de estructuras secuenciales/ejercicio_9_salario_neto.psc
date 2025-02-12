Algoritmo ejercicio_9_salario_neto

	Escribir 	"Escribe las horas trabajadas realizadas por el empleado"
	leer hTrabajadas
	Escribir 	"Escribe el precio de la hora laboral"
	leer pHora
    sBase <- hTrabajadas * pHora
    impuesto <- sBase * 0.20
    salarioNeto <- sBase - impuesto
    Escribir "Horas trabajadas: ", hTrabajadas
    Escribir "Precio por hora: ", pHora
    Escribir "Salario base: ", sBase
    Escribir "Descuento por impuestos (20%): ", impuesto
    Escribir "Salario neto a recibir: ", salarioNeto
FinAlgoritmo
