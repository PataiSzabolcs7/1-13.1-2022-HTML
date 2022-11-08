C = 10000
r = 8
m = 12
t = int (input("Kérjük ide írja be a futam időt (évben):"))
mt = m + t
FV = C*(1+r/m)**mt
print("Összeg:",FV)