Algoritmo ejercicio_14_calculo_pagar_luz
	Definir lecturaAnterior, lecturaActual, costoKilovatio, consumo, totalPagar Como Real
    
    Escribir "Ingrese la lectura anterior del medidor (en kWh):"
    Leer lecturaAnterior
    Escribir "Ingrese la lectura actual del medidor (en kWh):"
    Leer lecturaActual
    Escribir "Ingrese el costo por kilovatio-hora (COP/kWh):"
    Leer costoKilovatio
   
    consumo <- lecturaActual - lecturaAnterior
    totalPagar <- consumo * costoKilovatio
    
    Escribir "-------------------------------------------"
    Escribir "Consumo del mes: ", consumo, " kWh"
    Escribir "Monto total a pagar: ", totalPagar, " COP"
FinAlgoritmo
