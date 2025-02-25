P = int(input("Ingrese P: "))
Q = int(input("Ingrese Q: "))
if P**3 + Q**4 - 2 * P**2 > 680:
    print(f"P={P} y Q={Q} satisfacen la expresión")
else:
    print(f"P={P} y Q={Q} no satisfacen la expresión")