Algoritmo ejercicio_8
	Escribir 	"Escribe el valor del lado A del triangulo a calcular"
	leer a
	Escribir 	"Escribe el valor del lado B del triangulo a calcular"
	leer b
	Escribir 	"Escribe el valor del lado C del triangulo a calcular"
	leer c
    s <- (a + b + c) / 2
    area <- Raiz(s * (s - a) * (s - b) * (s - c))
    Escribir "Los lados del triángulo son: a=", a, ", b=", b, ", c=", c
    Escribir "El semiperímetro es: ", s
    Escribir "El área del triángulo es: ", area
FinAlgoritmo
