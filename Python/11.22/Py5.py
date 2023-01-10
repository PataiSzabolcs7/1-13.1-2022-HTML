import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else: 
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

u=[1 , 2, 1]
v=[1 , 4, 3]
T=[]


def vektorok_osszege(u, v):
    T.append(u[0]+v[0])
    T.append(u[1]+v[1])
    T.append(u[2]+v[2])
    return T

teszt(vektorok_osszege([u, v,1], [u, v,1]) == T )