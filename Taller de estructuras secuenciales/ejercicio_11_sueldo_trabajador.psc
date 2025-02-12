Algoritmo  sueldo_trabajador
	Definir nombre Como Cadena
    Definir horasNormales, pagoHora, horasExtras, numHijos Como Entero
    Definir sueldoBase, pagoHorasExtras, sueldoBruto Como Real
    Definir descuentoPagoForzoso, descuentoPolitica, descuentoCaja, totalDeducciones Como Real
    Definir actualizacionAcademica, primaPorHogar, asignacionHijos, totalAsignaciones Como Real
    Definir sueldoNeto Como Real
    
    Escribir "Ingrese el nombre del trabajador:"
    Leer nombre
    Escribir "Ingrese el número de horas normales trabajadas:"
    Leer horasNormales
    Escribir "Ingrese el pago por hora normal:"
    Leer pagoHora
    Escribir "Ingrese el número de horas extras trabajadas:"
    Leer horasExtras
    Escribir "Ingrese el número de hijos del trabajador:"
    Leer numHijos
    

    sueldoBase <- horasNormales * pagoHora
    
    pagoHorasExtras <- horasExtras * (pagoHora * 1.25)
    
    sueldoBruto <- sueldoBase + pagoHorasExtras
    
    descuentoPagoForzoso <- sueldoBase * 0.05
    descuentoPolitica <- sueldoBase * 0.02
    descuentoCaja <- sueldoBase * 0.07
    totalDeducciones <- descuentoPagoForzoso + descuentoPolitica + descuentoCaja
    
    
    actualizacionAcademica <- 250000
    primaPorHogar <- 180000
    asignacionHijos <- numHijos * 173000
    totalAsignaciones <- actualizacionAcademica + primaPorHogar + asignacionHijos
    
    sueldoNeto <- sueldoBruto + totalAsignaciones - totalDeducciones
    
    Escribir "-------------------------------------------"
    Escribir "Nombre del trabajador: ", nombre
    Escribir "Sueldo base: ", sueldoBase
    Escribir "Pago por horas extras: ", pagoHorasExtras
    Escribir "Sueldo bruto: ", sueldoBruto
    Escribir "Deducciones:"
    Escribir "  - Pago forzoso (5%): ", descuentoPagoForzoso
    Escribir "  - Política habitacional (2%): ", descuentoPolitica
    Escribir "  - Caja de ahorro (7%): ", descuentoCaja
    Escribir "  - Total deducciones: ", totalDeducciones
    Escribir "Asignaciones:"
    Escribir "  - Actualización académica: ", actualizacionAcademica
    Escribir "  - Prima por hogar: ", primaPorHogar
    Escribir "  - Asignación por hijos: ", asignacionHijos
    Escribir "  - Total asignaciones: ", totalAsignaciones
    Escribir "-------------------------------------------"
    Escribir "Sueldo neto a recibir en diciembre: ", sueldoNeto
FinAlgoritmo
