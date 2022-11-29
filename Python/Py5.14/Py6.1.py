xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for x in xs:
    if x >= 90:
        print("Jegy: Jeles")
    elif  80 <= x < 90:
        print("Jegy: Jó")
    elif 70 <= x <= 80:
        print("Jegy: Közepes")
    elif 60 <= x <= 70:
        print("Jegy: Elégséges")
    elif x >= 60:
        print("Jegy: Elégtelen")