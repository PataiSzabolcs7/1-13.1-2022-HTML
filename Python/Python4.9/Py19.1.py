import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
Sanyi.pensize(3)
Sanyi.speed(0.01)
for x in range(0, 5):
    Sanyi.forward(200)
    Sanyi.right(144)
kép.mainloop()
