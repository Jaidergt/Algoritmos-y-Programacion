Algoritmo ejercicio_17_presupuesto_hospital
	Definir presupuestoTotal, presupuestoGine, presupuestoTrauma, presupuestoPedia Como Real
    
    Escribir "Ingrese el presupuesto anual total del hospital (en COP):"
    Leer presupuestoTotal
    
    presupuestoGine <- presupuestoTotal * 0.40
    presupuestoTrauma <- presupuestoTotal * 0.30
    presupuestoPedia <- presupuestoTotal * 0.30
    
    Escribir "-------------------------------------------"
    Escribir "Presupuesto asignado a Ginecolog�a: ", presupuestoGine, " COP"
    Escribir "Presupuesto asignado a Traumatolog�a: ", presupuestoTrauma, " COP"
    Escribir "Presupuesto asignado a Pediatr�a: ", presupuestoPedia, " COP"
FinAlgoritmo
