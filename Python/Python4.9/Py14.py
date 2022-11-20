import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("Hotpink")
Sanyi.pensize(3)
def negyzet(t,h):
    for x in range(0,4):
        t.forward(h)
        t.left(90)
    Sanyi.penup()
    Sanyi.right(135)
    Sanyi.forward(15)
    Sanyi.right(135)
    Sanyi.pendown()
def negyzet2(b,a):
    for x in range(4):
        b.forward(a)
        b.right(90)
    Sanyi.penup()
    Sanyi.left(135)
    Sanyi.forward(15)
    Sanyi.left(135)
    Sanyi.pendown()
meret = 20
for x in range(3):
    negyzet(Sanyi, meret)
    meret = meret + 20
    negyzet2(Sanyi, meret)
    meret = meret + 20
kép.mainloop()

