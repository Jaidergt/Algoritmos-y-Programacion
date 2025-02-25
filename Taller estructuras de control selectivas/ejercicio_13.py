from datetime import datetime
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")
dia, mes, año = map(int, fecha_nacimiento.split('/'))
edad = datetime.now().year - anio
signos = [(21, 3, "Aries"), (20, 4, "Tauro"), (21, 5, "Géminis"), (22, 6, "Cáncer"), (23, 7, "Leo"), (24, 8, "Virgo"), (23, 9, "Libra"), (23, 10, "Escorpio"), (22, 11, "Sagitario"), (22, 12, "Capricornio"), (20, 1, "Acuario"), (19, 2, "Piscis")]
signo = next(s for d, m, s in signos if (mes == m and dia >= d) or (mes == (m % 12 + 1) and dia < d))
print(f"Edad: {edad}, Signo: {signo}")