Algoritmo ejercicio_16
	Definir galonesSurtidos, litrosSurtidos, precioLitro, totalPagar Como Real
    
    
    precioLitro <- 50000  
    
    Escribir "Ingrese la cantidad de galones surtidos:"
    Leer galonesSurtidos
    
    litrosSurtidos <- galonesSurtidos * 3.785
    
    totalPagar <- litrosSurtidos * precioLitro
    
    Escribir "-------------------------------------------"
    Escribir "Cantidad surtida en litros: ", litrosSurtidos, " L"
    Escribir "Monto total a pagar: ", totalPagar, " COP"
FinAlgoritmo
