import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
Sanyi.pensize(3)
Sanyi.speed(0.1)
meret = 5
def spiral(t,h):
    t.forward(h)
    t.right(90)
for x in range (100):
    spiral(Sanyi,meret)
    meret = meret + 5
    Sanyi.left(1)
kép.mainloop()