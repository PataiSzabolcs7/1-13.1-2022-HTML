import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else: 
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)
s=5,3,7
v=[1,2,]
T=[]

def szorzas_skalarral(s,v):
    T.append(s*v[0])
