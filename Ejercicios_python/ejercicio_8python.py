import math

def area_triangulo(a, b, c):
    # Calculamos el semiperímetro
    s = (a + b + c) / 2
    # Aplicamos la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Ejemplo de uso
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

# Verificamos si los lados forman un triángulo válido
if a + b > c and a + c > b and b + c > a:
    print(f"El área del triángulo es: {area_triangulo(a, b, c):.2f}")
else:
    print("Los lados ingresados no forman un triángulo válido.")