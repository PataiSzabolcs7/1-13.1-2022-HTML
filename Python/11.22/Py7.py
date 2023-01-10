import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else: 
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

u=[1,2, 1]
v=[1,4, 3]
T=[]
p=[]
def szorzas_skalarral(u,v):
    for x in range(len(v)):
        T.append(u[x]*v[x])
        p=0
    for szám in T:
        p+=szám
    print(p)
    return(T)
teszt(szorzas_skalarral(u,v)== T)
