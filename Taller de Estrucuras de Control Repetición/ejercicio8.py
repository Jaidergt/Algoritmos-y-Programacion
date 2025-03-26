total_licor = 0
mujeres_menores = 0
hombres_no_aguardiente = 0
total_cerveza = 0
suma_edades_cerveza = 0
total_whisky = 0
total_personas = 0

while True:
    licor = input("¿Consume licor? (Sí/No): ").strip().lower()
    if licor == "sí":
        total_licor += 1
        tipo = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
    else:
        tipo = 0

    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    if sexo == "F" and edad < 18:
        mujeres_menores += 1

    if sexo == "M" and tipo != 1 and 20 <= edad <= 25:
        hombres_no_aguardiente += 1

    if tipo == 3:
        total_cerveza += 1
        suma_edades_cerveza += edad

    if tipo == 5:
        total_whisky += 1

    total_personas += 1

    continuar = input("¿Desea continuar? (Sí/No): ").strip().lower()
    if continuar == "no":
        break

print("Total que consume licor:", total_licor)
print("Mujeres menores de edad:", mujeres_menores)
print("Hombres que no consumen aguardiente y tienen entre 20 y 25:", hombres_no_aguardiente)
if total_cerveza > 0:
    print("Promedio edad consumidores de cerveza:", suma_edades_cerveza / total_cerveza)
print("Porcentaje de whisky:", (total_whisky / total_personas) * 100 if total_personas > 0 else 0, "%")