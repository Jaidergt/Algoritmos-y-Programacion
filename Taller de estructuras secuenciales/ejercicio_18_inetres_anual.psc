Algoritmo ejercicio_18_inetres_anual
	Definir capital, interesPagado, tiempo, tasaInteres Como Real
    
    Escribir "Ingrese el capital prestado (en Bol�vares):"
    Leer capital
    Escribir "Ingrese el inter�s total pagado (en Bol�vares):"
    Leer interesPagado
    tiempo <- 4 

    tasaInteres <- (interesPagado * 100) / (capital * tiempo)  
	
    Escribir "-------------------------------------------"
    Escribir "El porcentaje de inter�s anual cobrado fue: ", tasaInteres, " %"
FinAlgoritmo
