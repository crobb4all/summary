import turtle

# Создаем экран
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Простая рыба")

# Создаем черепаху
fish = turtle.Turtle()
fish.speed(2)  # Задаем скорость черепахи

# тело
fish.fillcolor("blue")
fish.begin_fill()
fish.circle(50)  # тело рыбы
fish.end_fill()

# хвост
fish.penup()
fish.goto(-34, 20)
fish.pendown()
fish.setheading(240)
fish.fillcolor("blue")
fish.begin_fill()
for _ in range(2):
    fish.forward(50)
    fish.right(120)
fish.end_fill()

# Глаз
fish.penup()
fish.goto(15, 60)
fish.pendown()
fish.fillcolor("white")
fish.begin_fill()
fish.circle(5)  # глаз
fish.end_fill()
# Зрачок
fish.penup()
fish.goto(17, 63)
fish.pendown()
fish.fillcolor("black")
fish.begin_fill()
fish.circle(2)  # зрачок
fish.end_fill()

# Рот
fish.penup()
fish.goto(20, 40)
fish.pendown()
fish.setheading(-35)
fish.circle(20, 90)  # рот

fish.hideturtle()
screen.mainloop()