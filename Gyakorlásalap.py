a = int (input("Adj meg egy számot:"))
b = int (input("Add meg a második számot:"))
if a<=0 and b<=0:
    print("Mind kettő negatív")
elif a<0 and b>0:
    print("Az első szám negatív")
elif a>0 and b<0:
    print("A Második szám negatív")
elif a>=0 and b<=0:
    print("Egyik se negatív")
