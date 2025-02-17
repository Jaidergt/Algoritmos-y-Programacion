asas_cambio = {
    "chelin_austriaco_a_peseta": 956.871 / 100,  # 100 chelines = 956.871 pesetas
    "dracma_griego_a_peseta": 88.607 / 100,  # 100 dracmas = 88.607 pesetas
    "peseta_a_dolar": 1 / 122.499,  # 1 dólar = 122.499 pesetas
    "peseta_a_lira_italiana": 100 / 9.289,  # 100 liras = 9.289 pesetas
    "peseta_a_franco_frances": 1 / 20.110  # 1 franco francés = 20.110 pesetas
}

# 1. Leer cantidad en chelines austriacos y convertir a pesetas
chelines = float(input("Ingrese la cantidad en chelines austriacos: "))
pesetas_chelines = chelines * tasas_cambio["chelin_austriaco_a_peseta"]
print(f"{chelines} chelines austríacos equivalen a {pesetas_chelines:.2f} pesetas.")

# 2. Leer cantidad en dracmas griegos y convertir a francos franceses
dracmas = float(input("\nIngrese la cantidad en dracmas griegos: "))
pesetas_dracmas = dracmas * tasas_cambio["dracma_griego_a_peseta"]
francos_franceses = pesetas_dracmas * tasas_cambio["peseta_a_franco_frances"]
print(f"{dracmas} dracmas griegos equivalen a {francos_franceses:.2f} francos franceses.")

# 3. Leer cantidad en pesetas y convertir a dólares y liras italianas
pesetas = float(input("\nIngrese la cantidad en pesetas: "))
dolares = pesetas * tasas_cambio["peseta_a_dolar"]
liras_italianas = pesetas * tasas_cambio["peseta_a_lira_italiana"]
print(f"{pesetas} pesetas equivalen a {dolares:.2f} dólares estadounidenses.")
print(f"{pesetas} pesetas equivalen a {liras_italianas:.2f} liras italianas.")