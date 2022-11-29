a = int (input("Adja meg az eléret pontszámot:"))
if a >= 90:
    print("Jegy: Jeles")
elif  80 <= a < 90:
    print("Jegy: Jó")
elif 70 <= a <= 80:
    print("Jegy: Közepes")
elif 60 <= a <= 70:
    print("Jegy: Elégséges")
elif a >= 60:
    print("Jegy: Elégtelen")