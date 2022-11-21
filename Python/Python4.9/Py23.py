def sokszog_rajzolas(t, n, sz):
    for x in range(n):
        t.forward(100)
        t.left(sz)

import turtle
kép = turtle.Screen()
Eszti = turtle.Turtle()
kép.bgcolor("lightgreen")
Eszti.color("Hotpink")
Eszti.pensize(3)

sokszog_rajzolas(Eszti,8, 50)

kép.mainloop()