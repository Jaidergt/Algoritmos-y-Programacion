Algoritmo  ejercicio_13_calculo_banco
	Definir N1, N2, N3, N4, N5, N6, N7, N8 Como Entero
    Definir total Como Real
    
    
    Escribir "Ingrese la cantidad de billetes de 50,000:"
    Leer N1
    Escribir "Ingrese la cantidad de billetes de 20,000:"
    Leer N2
    Escribir "Ingrese la cantidad de billetes de 10,000:"
    Leer N3
    Escribir "Ingrese la cantidad de billetes de 5,000:"
    Leer N4
    Escribir "Ingrese la cantidad de billetes de 2,000:"
    Leer N5
    Escribir "Ingrese la cantidad de billetes de 1,000:"
    Leer N6
    Escribir "Ingrese la cantidad de billetes de 500:"
    Leer N7
    Escribir "Ingrese la cantidad de billetes de 100:"
    Leer N8
  
    total <- (N1 * 50000) + (N2 * 20000) + (N3 * 10000) + (N4 * 5000) + (N5 * 2000) + (N6 * 1000) + (N7 * 500) + (N8 * 100)
   
    Escribir "-------------------------------------------"
    Escribir "El total de dinero en el banco es: ", total, " COP"
FinAlgoritmo
