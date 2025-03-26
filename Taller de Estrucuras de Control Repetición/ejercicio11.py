saldo = 1000  # Saldo inicial

while True:
    print("\n1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        deposito = float(input("Ingrese el monto a depositar: "))
        saldo += deposito
    elif opcion == 2:
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
        else:
            print("Saldo insuficiente")
    elif opcion == 3:
        print("Saldo actual:", saldo)
    elif opcion == 4:
        print("Gracias por usar el cajero")
        break
    else:
        print("Opción no válida")