Algoritmo ejercicio_9
	Escribir "Ingrese un n�mero:"
	Leer num
	numTexto <- ConvertirATexto(num)
	numReverso <- ""
	
	Para i <- Longitud(numTexto) Hasta 1 Con Paso -1 Hacer
		numReverso <- Concatenar(numReverso, Subcadena(numTexto, i, i))
	FinPara
	
	Si numTexto = numReverso Entonces
		Escribir "Es un pal�ndrome"
	Sino
		Escribir "No es un pal�ndrome"
	FinSi
	
FinAlgoritmo
