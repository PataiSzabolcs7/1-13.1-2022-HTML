xs = [160, -43, 270, -97, -43, 200, -940, 17,-86]
from random import randrange
import turtle
kép=turtle.Screen()
Kalóz= turtle.Turtle()
for x in xs:
    Kalóz.forward(100)
    if x>0:
        Kalóz.left(x)
    else:
        Kalóz.right(x)
print("Kalóz ebbe az írányba néz:",x)
kép.mainloop()