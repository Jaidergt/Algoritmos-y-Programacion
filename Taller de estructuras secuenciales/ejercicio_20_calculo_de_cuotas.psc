Algoritmo ejercicio_20_calculo_de_cuotas
	Definir P, T, precioTotalCuotas, recargo, porcentajeRecargo Como Real
	
    Escribir "Ingrese el precio del computador al contado (P):"
    Leer P
    Escribir "Ingrese el valor de cada cuota mensual (T):"
    Leer T
	
    precioTotalCuotas <- T * 12
	
    recargo <- precioTotalCuotas - P
	
    porcentajeRecargo <- (recargo / P) * 100
	
    Escribir "-------------------------------------------"
    Escribir "Precio al contado: ", P, " COP"
    Escribir "Precio total con cuotas: ", precioTotalCuotas, " COP"
    Escribir "Recargo total: ", recargo, " COP"
    Escribir "Porcentaje de recargo: ", porcentajeRecargo, " %"
FinAlgoritmo
