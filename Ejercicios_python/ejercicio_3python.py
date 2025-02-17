sueldo_base = float(input("Ingresa el sueldo base del vendedor: "))
venta1 = float(input("Ingresa el monto de la primera venta: "))
venta2 = float(input("Ingresa el monto de la segunda venta: "))
venta3 = float(input("Ingresa el monto de la tercera venta: "))

# Calcular las comisiones (10% de cada venta)
comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10


total_comisiones = comision1 + comision2 + comision3


total_recibido = sueldo_base + total_comisiones


print("El total de comisiones es: $", total_comisiones)
print("El total que recibirá el vendedor es: $", total_recibido)
