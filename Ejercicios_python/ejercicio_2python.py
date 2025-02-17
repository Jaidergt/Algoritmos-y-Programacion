capital_inicial = float(input("Ingresa el capital inicial que deseas invertir: "))

tasa_interes = 0.02

ganancia = capital_inicial * tasa_interes
capital_final = capital_inicial + ganancia

print("La ganancia después de un mes será: $", ganancia)
print("El capital final después de un mes será: $", capital_final)