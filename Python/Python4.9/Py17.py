import turtle
kép = turtle.Screen()
Sanyi = turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
Sanyi.pensize(3)
Sanyi.speed(0.1)
def poligon_rajzolas(t):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
def szabalyos_haromszog_rajzolas(t,sz):
    for x in range (sz):
        poligon_rajzolas(t)

szabalyos_haromszog_rajzolas(Sanyi,1)

    
kép.mainloop()
