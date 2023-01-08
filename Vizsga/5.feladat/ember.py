from random import randint
from emberekalap import Ember
r=None
for x in range(3):
    a=input("Add meg a nevet!")
    b=input("Add meg a foglalkozást!")
    c=input("Add meg a nemét!(f/n)")
    szam=randint(0,50)
    if c=="f":
        c="férfi"
    elif c=="n":
        c="nő"
    e=Ember(a,b,c)
    print(f"{e.getNEV()} {e.getNEM()}, {e.getFOG()}, szerencse száma a {szam}")
    


