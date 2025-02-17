def calcular_salario(nombre, horas_normales, pago_hora, horas_extras, num_hijos):
    # Cálculo del sueldo base
    sueldo_base = horas_normales * pago_hora

    # Cálculo del pago por horas extras (25% más del pago normal)
    pago_hora_extra = pago_hora * 1.25
    total_horas_extras = horas_extras * pago_hora_extra

    # Asignaciones
    actualizacion_academica = 250000
    asignacion_por_hijos = num_hijos * 173000
    prima_hogar = 180000
    total_asignaciones = sueldo_base + total_horas_extras + actualizacion_academica + asignacion_por_hijos + prima_hogar

    # Deducciones
    pago_forzoso = sueldo_base * 0.05
    politica_habitacional = sueldo_base * 0.02
    caja_ahorro = sueldo_base * 0.07
    total_deducciones = pago_forzoso + politica_habitacional + caja_ahorro

    # Cálculo del sueldo neto
    sueldo_neto = total_asignaciones - total_deducciones

    # Mostrar resultados
    print("\n--- RESUMEN DE PAGO PARA:", nombre, "---")
    print(f"Sueldo base: ${sueldo_base:,.2f}")
    print(f"Pago por horas extras: ${total_horas_extras:,.2f}")
    print(f"Asignación por actualización académica: ${actualizacion_academica:,.2f}")
    print(f"Asignación por hijos ({num_hijos} hijos): ${asignacion_por_hijos:,.2f}")
    print(f"Prima por hogar: ${prima_hogar:,.2f}")
    print(f"Total asignaciones: ${total_asignaciones:,.2f}")
    print("\n--- DEDUCCIONES ---")
    print(f"Pago forzoso (5% del sueldo base): ${pago_forzoso:,.2f}")
    print(f"Política habitacional (2% del sueldo base): ${politica_habitacional:,.2f}")
    print(f"Caja de ahorro (7% del sueldo base): ${caja_ahorro:,.2f}")
    print(f"Total deducciones: ${total_deducciones:,.2f}")
    print("\n--- SUELDO NETO ---")
    print(f"Sueldo neto del trabajador: ${sueldo_neto:,.2f}")

# Solicitar datos al usuario
nombre = input("Ingrese el nombre del trabajador: ")
horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
pago_hora = float(input("Ingrese el pago por hora normal: "))
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
num_hijos = int(input("Ingrese el número de hijos: "))

# Calcular y mostrar el sueldo
calcular_salario(nombre, horas_normales, pago_hora, horas_extras, num_hijos)