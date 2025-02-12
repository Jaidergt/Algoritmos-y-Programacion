Algoritmo ejercicio_18_inetres_anual
	Definir capital, interesPagado, tiempo, tasaInteres Como Real
    
    Escribir "Ingrese el capital prestado (en Bolívares):"
    Leer capital
    Escribir "Ingrese el interés total pagado (en Bolívares):"
    Leer interesPagado
    tiempo <- 4 

    tasaInteres <- (interesPagado * 100) / (capital * tiempo)  
	
    Escribir "-------------------------------------------"
    Escribir "El porcentaje de interés anual cobrado fue: ", tasaInteres, " %"
FinAlgoritmo
