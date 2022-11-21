def HoE(a):
    b = False
    if a > 150:
        b=True
    return b
a = input("Cím:")
while(a!=""):
    b = int (input("Oldalak:"))
    old = HoE(b)
    if old:
        print("A Könyv hosszú")
    else:
        print("Könyv nem hosszú")