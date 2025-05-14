resultados = []

C = int(input(""))
for i in range(C):
    datos = input()
    (a, N) = datos.split()
    (a) = str(a)
    (N) = int(N)
    if  a == "Thor":
        resultados.append("Y")
    else:
        resultados.append("N")

for valores in resultados:
    print(valores)