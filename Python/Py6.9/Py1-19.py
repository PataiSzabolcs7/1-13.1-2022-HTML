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
    teszt(nap_nev(a) == "Hétfő")
elif a == 1:
    teszt(nap_nev(a) == "Kedd")
elif a == 2:
    teszt(nap_nev(a) == "Szerda")
elif a == 3:
    teszt(nap_nev(a) == "Csütörtök")
elif a == 4:
    teszt(nap_nev(a) == "Péntek")
elif a == 5:
    teszt(nap_nev(a) == "Szombat")
elif a == 6:
    teszt(nap_nev(a) == "Vasárnap")
elif a > 6:
    teszt(nap_nev(a) == None)

#3.Feladat
a = (input("Írj be egy Napot!:"))
def nap_sorszam(a):
    if a == "Hétfő":
        a = 0
        print("Nap száma:",a)
        return a
    elif a == "Kedd":
        a = 1
        print("Nap száma:",a)
        return a
    elif a == "Szerda":
        a = 2
        print("Nap száma:",a)
        return a
    elif a == "Csütörtök":
        a = 3
        print("Nap száma:",a)
        return a
    elif a == "Péntek":
        a = 4
        print("Nap száma:",a)
        return a
    elif a == "Szombat":
        a = 5
        print("Nap száma:",a)
    elif a == "Vasárnap":
        a = 6
        print("Nap száma:",a)
        return a
    elif int:
        return a
    elif a!= "Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
        return a

if a == "Hétfő":
    teszt(nap_sorszam(a) == 0)
elif a == "Kedd":
    teszt(nap_sorszam(a) == 1)
elif a == "Szerda":
    teszt(nap_sorszam(a) == 2)
elif a == "Csütörtök":
    teszt(nap_sorszam(a) == 3)
elif a == "Péntek":
    teszt(nap_sorszam(a) == 4)
elif a == "Szombat":
    teszt(nap_sorszam(a) == 5)
elif a == "Vasárnap":
    teszt(nap_sorszam(a) == 6)
elif a == "Halloween":
    teszt(nap_sorszam(a) == None)
elif int:
    teszt(nap_sorszam(a) == a)
elif a =="Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
    teszt(nap_sorszam(a) == a)
 
#4 Feladat
z = input("Melyik napot választod?")
y = int(input("Hány nap múlva mész nyaralni?:"))

if z == "Hétfő":
    z = 0
elif z == "Kedd":
    z = 1
elif z == "Szerda":
    z = 2
elif z == "Csütörtök":
    z = 3
elif z == "Péntek":
    z = 4
elif z == "Szombat":
    z = 5
elif z == "Vasárnap":
    z = 6

x = 0
def napok_hozzaadasa(z,y):
    x = z + y
    if x == 0:
        x = "Hétfő"
    elif x == 1:
        x = "Kedd"
    elif x == 2:
        x = "Szerda"
    elif x == 3:
        x = "Csütörtök"
    elif x == 4:
        x = "Péntek"
    elif x == 5:
        x = "Szombat"
    elif x == 6:
        x = "Vasárnap"
    print(x)
    return z + y == x
teszt(napok_hozzaadasa(z,y) == x)