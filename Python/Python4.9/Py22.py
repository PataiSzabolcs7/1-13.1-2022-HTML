import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("Hotpink")
Sanyi.pensize(3)
def negyzet(t,h):
   for x in range(5):
       t.forward(h)
       t.left(90)
meret = 20
for x in range(5):
    negyzet(Sanyi,meret)
    Sanyi.right(90)
    Sanyi.penup()
    Sanyi.forward(15)
    Sanyi.pendown()
kép.mainloop()