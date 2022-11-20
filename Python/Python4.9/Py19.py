import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
Sanyi.pensize(3)
Sanyi.speed(0.01)
def pentagrama(t):
    for x in range(0, 5):
        t.forward(200)
        t.right(144)

for x in range(5):
    pentagrama(Sanyi)
    Sanyi.penup()
    Sanyi.forward(650)
    Sanyi.right(144)
    Sanyi.pendown()


pentagrama(Sanyi)
kép.mainloop()
