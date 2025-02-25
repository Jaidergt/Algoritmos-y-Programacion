dias = int(input("Ingrese la cantidad de días de alquiler: "))
costo_dia = float(input("Ingrese el costo diario del alquiler: "))
descuento = 0
if dias > 7:
    descuento = 0.10
elif dias > 3:
    descuento = 0.05
total = dias * costo_dia * (1 - descuento)
print(f"Total a pagar por el alquiler: {total}")