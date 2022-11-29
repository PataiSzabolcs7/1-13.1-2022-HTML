import turtle
def rajzolj_oszlopot(t, magassag):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.pensize(3)
xs = [48,117,200,240,160,260,220]
for m in xs:
    if m > 200:
        Eszti.color("Blue","Red")
    elif 100 < m < 200:
        Eszti.color("Blue","Yellow")
    elif m < 100:
        Eszti.color("Blue","Green")
    rajzolj_oszlopot(Eszti, m)
ablak.mainloop()
