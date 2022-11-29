a = int(input("Írja be az első számot:"))
b = int(input("Írja be a második számot:"))
c = int(input("Írja be az harmadik számot(legnagyobbnak kell lennie):"))
def derekszogu_e(a,b,c):
    if (a**2+b**2 == c**2):
        print(a**2+b**2 == c**2)
    elif (a**2+b**2 != c**2):
        print(a**2+b**2 == c**2)
derekszogu_e(a,b,c) 