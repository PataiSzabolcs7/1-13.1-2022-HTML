import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.color("hotpink")
kép.bgcolor("lightgreen")
def negyzet(t):
    for x in range(0,4):
      t.forward(20)
      t.left(90)
for x in range(0,5):
    negyzet(Sanyi)
    Sanyi.penup()
    Sanyi.forward(40)
    Sanyi.pendown()
kép.mainloop()