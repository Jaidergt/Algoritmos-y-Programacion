import turtle
screen = turtle.Screen()
screen.bgcolor("black")
colores = ["cyan", "green", "magenta", "blue", "yellow", "red"]
escritor = turtle.Turtle()
escritor.hideturtle()
escritor.penup()
escritor.goto(-180, 0)  # Posición inicial
escritor.pensize(3)
escritor.speed(0)

nombre = "JAIDER"
for i, letra in enumerate(nombre):
    escritor.color(colores[i % len(colores)])
    escritor.write(letra, font=("Arial", 60, "bold"))
    escritor.forward(60)  # Espacio entre letras

turtle.done()