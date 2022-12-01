import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)
def abszolut_ertek(n):
    if n < 0:
        return 1
    elif n > 0:
        return n
#1 Feladat
n=input("Írj be egy égtáj rövidítését:")
def fordulj_orjarasi_iranyaba(sky):
    if sky=="É":
        print("K")
        return sky
    elif sky == "Ny":
        print("É")
        return sky
    elif sky == "D":
        print("Ny")
        return sky
    elif sky == "K":
        print("D")
        return sky
    elif sky == int:
        sky == None
        return sky
teszt(fordulj_orjarasi_iranyaba(n)== n or fordulj_orjarasi_iranyaba(n)!=n)

#2 Feladat
a = int(input("Írj be egy számot 0-6-ig:"))
def nap_nev(a):
    if a == 0:
        a = "Hétfő"
        print("Hétfői Nap")
        return a
    elif a == 1:
        a = "Kedd"
        print("Keddi Nap")
        return a
    elif a == 2:
        a = "Szerda"
        print("Szerdai Nap")
        return a
    elif a == 3:
        a = "Csütörtök"
        print("Csütörtöki Nap")
        return a
    elif a == 4:
        a = "Péntek"
        print("Pénteki Nap")
        return a
    elif a == 5:
        a = "Szombat"
        print("Szombati Nap")
    elif a == 6:
        a = "Vasárnap"
        print("Vasárnapi nap")
        return a
if a == 0:
    teszt(nap_nev(a) == "Hétfői nap")
elif a == 1:
    teszt(nap_nev(a) == "Keddi  nap")
elif a == 2:
    teszt(nap_nev(a) == "Szerdai nap")
elif a == 3:
    teszt(nap_nev(a) == "Csütörtöki nap")
elif a == 4:
    teszt(nap_nev(a) == "Pénteki nap")
elif a == 5:
    teszt(nap_nev(a) == "Szombati nap")
elif a == 6:
    teszt(nap_nev(a) == "Vasárnapi nap")
elif a > 6:
    teszt(nap_nev(a) == None)