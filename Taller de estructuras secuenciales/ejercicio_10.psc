Algoritmo  ejercicio_10
    
    Escribir "Seleccione la moneda a convertir a pesetas:"
    Escribir "1. 100 chelines austríacos"
    Escribir "2. 1 dólar estadounidense"
    Escribir "3. 100 dracmas griegos"
    Escribir "4. 100 francos belgas"
    Escribir "5. 1 franco francés"
    Escribir "6. 1 libra esterlina"
    Escribir "7. 100 liras italianas"
    Leer opcion
    
    Escribir "Ingrese la cantidad a convertir:"
    Leer cantidad
    
    Segun opcion Hacer
        1:
            conversion <- cantidad * (956.871 / 100)
        2:
            conversion <- cantidad * 122.499
        3:
            conversion <- cantidad * (88.607 / 100)
        4:
            conversion <- cantidad * (323.728 / 100)
        5:
            conversion <- cantidad * 20.110
        6:
            conversion <- cantidad * 178.938
        7:
            conversion <- cantidad * (9.289 / 100)
        De Otro Modo:
            Escribir "Opción no válida."
            conversion <- 0
    FinSegun
    
    Si conversion > 0 Entonces
        Escribir "El equivalente en pesetas es: ", conversion
    FinSi
FinAlgoritmo
