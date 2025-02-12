Algoritmo ejercicio_21_recargo_por_cuotas
	Definir P, T Como Real
    Definir totalCuotas, recargo, porcentajeRecargo Como Real
	
    Escribir "Ingrese el precio del computador al contado (P en COP):"
    Leer P
    Escribir "Ingrese el valor de cada cuota mensual (T en COP):"
    Leer T
	
    totalCuotas <- T * 12

    recargo <- totalCuotas - P
	
    porcentajeRecargo <- (recargo / P) * 100
	
    Escribir "Costo total en cuotas: ", totalCuotas, " COP"
    Escribir "Recargo total: ", recargo, " COP"
    Escribir "Porcentaje de recargo sobre el pago al contado: ", porcentajeRecargo, "%"
FinAlgoritmo
