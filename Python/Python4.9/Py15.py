import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
Sanyi.pensize(3)
for x in range (5):
    for x in range(4):
        Sanyi.forward(100)
        Sanyi.left(90)
        Sanyi.forward(100)
        Sanyi.backward(200)
        Sanyi.forward(100)
        Sanyi.right(90)
        Sanyi.backward(100)
        Sanyi.left(90)
    Sanyi.left(36)
kép.mainloop()