Algoritmo ejercicio_17_presupuesto_hospital
	Definir presupuestoTotal, presupuestoGine, presupuestoTrauma, presupuestoPedia Como Real
    
    Escribir "Ingrese el presupuesto anual total del hospital (en COP):"
    Leer presupuestoTotal
    
    presupuestoGine <- presupuestoTotal * 0.40
    presupuestoTrauma <- presupuestoTotal * 0.30
    presupuestoPedia <- presupuestoTotal * 0.30
    
    Escribir "-------------------------------------------"
    Escribir "Presupuesto asignado a Ginecología: ", presupuestoGine, " COP"
    Escribir "Presupuesto asignado a Traumatología: ", presupuestoTrauma, " COP"
    Escribir "Presupuesto asignado a Pediatría: ", presupuestoPedia, " COP"
FinAlgoritmo
