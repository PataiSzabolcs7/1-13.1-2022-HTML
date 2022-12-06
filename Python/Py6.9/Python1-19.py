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
print("1.feladat")
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
print("2.feladat")
a = int(input("Írj be egy számot 0-6-ig:"))
def nap_nev(a):
    if a == 0:
        a = "Hétfő"
        print("Hétfő")
        return a
    elif a == 1:
        a = "Kedd"
        print("Kedd")
        return a
    elif a == 2:
        a = "Szerda"
        print("Szerda")
        return a
    elif a == 3:
        a = "Csütörtök"
        print("Csütörtök")
        return a
    elif a == 4:
        a = "Péntek"
        print("Péntek")
        return a
    elif a == 5:
        a = "Szombat"
        print("Szombat")
    elif a == 6:
        a = "Vasárnap"
        print("Vasárnap")
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
print("3.feladat")
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
    elif int or a!= "Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
        return None

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
elif a == int or a!= "Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
    teszt(nap_sorszam(a) == None )
 
#4 Feladat
print("4.feladat")
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
    while x>6:
        x=x-7
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

#5 Feladat(rossz).
print("5 feladat(Nincs kész)")
z = input("Melyik napot választod?")
y = int(input("Hány nappal vissza akarsz számolni?:"))
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
    x = z - y
    while x > 6:
        x=x%7
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
    return z - y == x
teszt(napok_hozzaadasa(z,y) == x)

#6.Feladat
print("6.Feladat")
q = input("Melyik hónapot választod?")
def honap_napja(q):
    if q == "Január":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Február":
        q = 28
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Március":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Április":
        q = 30
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Május":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Június":
        q = 30
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Július":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Agusztus":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Szeptember":
        q = 30
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "Október":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "November":
        q = 30
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif q == "December":
        q = 31
        print(f"Ez a hónap  ennyi napos:{q} ")
        return q
    elif int or q !="Január""Február""Március""Április""Május""Június""Július""Agusztus""Szeptember""Október""November""December":
        return None

if q == "Január":
    teszt(honap_napja(q) == 31)
elif q =="Február":
    teszt(honap_napja(q) == 28)
elif q =="Március":
    teszt(honap_napja(q) == 31)
elif q =="Április":
    teszt(honap_napja(q) == 30)
elif q =="Május":
    teszt(honap_napja(q) == 31)
elif q =="Június":
    teszt(honap_napja(q) == 30)
elif q =="Július":
    teszt(honap_napja(q) == 31)
elif q =="Agusztus":
    teszt(honap_napja(q) == 31)
elif q =="Szeptember":
    teszt(honap_napja(q) == 30)
elif q =="Október":
    teszt(honap_napja(q) == 31)
elif q =="November":
    teszt(honap_napja(q) == 30)
elif q =="December":
    teszt(honap_napja(q) == 31)

#7.feladat
print("7.Feladat")
a = int(input("Hány Óra? :"))
b = int(input("Hány Perc? :"))
c = int(input("Hány Másodperc? :"))
y = 0
def masodperc_valtas(a,b,c):
    a = a*3600
    b = b*60
    c = c
    y = a + b + c
    print(y)
    return 0
teszt(masodperc_valtas(a,b,c) == y) 

#8.Feladat
print("8.Feladat")
a=float(input("Hány Óra? : "))
b=float(input("Hány Perc? : "))
c=float(input("Hány Másodperc? : "))
y=0
def masodperc_valtas(a,b,c):
    a=a*3600
    b=b*60
    c=c
    y=a+b+c
    print(int(y))
    return 0
teszt(masodperc_valtas(a, b, c) == y)

#9.Feladat
print("9.Feladat")

#10. Feladat
print("10.Feladat")
teszt(3 % 4 == 0)                  #Azért nem jó, mert nincs maradék
teszt(3 % 4 == 3)                  #Jó
teszt(3 / 4 == 0)                  #Azért nem jó, mert az érték 0.75
teszt(3 // 4 == 0)                 #Jó
teszt(3+4*2 == 14)                 #Azért nem jó, mert az összeg nem egyenlő 14-el
teszt(4-2+2 == 0)                  #Azért nem jó, mert az összeg nem egyenlő 0-al
teszt(len("helló, világ!") == 13)  #jó

#11.Feladat
print("11.Feladat")
a=int(input("Első szám: "))
b=int(input("Második szám: "))
def oh(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    elif a<b:
        return -1
if a>b:
    teszt(oh(a, b) == 1)
elif a==b:
    teszt(oh(a, b) == 0)
elif a<b:
    teszt(oh(a, b) == -1)

#12.Feladat
print("12.Feladat")
a=int(input("írd be az első befogót:"))
b=int(input("írd be a második befogót:"))
c=0
def atfogo(c,a,b):
    c=a**2+b**2
    print(c**0.5)
    return 0
teszt(atfogo(a, b) == c)