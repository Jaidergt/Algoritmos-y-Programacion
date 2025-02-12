Algoritmo ejercicio_15
	Definir precioFinal, PVP, descuento, porcentajeDescuento Como Real
    
    Escribir "Ingrese el precio de venta al público (PVP) del producto:"
    Leer PVP
    Escribir "Ingrese el precio final pagado por el producto:"
    Leer precioFinal
    
    descuento <- PVP - precioFinal
    porcentajeDescuento <- (descuento / PVP) * 100
    
    Escribir "-------------------------------------------"
    Escribir "Descuento aplicado: ", descuento, " COP"
    Escribir "Porcentaje de descuento: ", porcentajeDescuento, " %"
FinAlgoritmo
