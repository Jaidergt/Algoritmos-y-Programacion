metros = float(input("Ingresa la cantidad en metros: "))

pulgadas = metros * 39.27

pies = int(pulgadas // 12)  
pulgadas_restantes = pulgadas % 12  

print(f"{metros} metros son equivalentes a {pies} pies y {pulgadas_restantes:.2f} pulgadas.")