import turtle
kép= turtle.Screen()
Sanyi=turtle.Turtle()
Sanyi.stamp()
Sanyi.shape("turtle")
Sanyi.color("lightgreen")
for x in range (0,12):
    Sanyi.penup()
    Sanyi.forward(100)
    Sanyi.pendown()
    Sanyi.forward(10)
    Sanyi.penup()
    Sanyi.forward(15)
    Sanyi.pendown()
    Sanyi.stamp()
    Sanyi.penup()
    Sanyi.backward(125)
    Sanyi.pendown()
    Sanyi.left(30)
kép.mainloop()