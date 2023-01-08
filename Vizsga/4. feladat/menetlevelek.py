from Classes import Menetlevél
v=None
T=[]
def fogyasztás(v):
        a=input("Rendszám: ")
        b=input("Megtett km: ")
        c=input("Összes üzemanyag fogyasztás: ")
        T.append(a)
        T.append(b)
        T.append(c)
fogyasztás(v)
print(T)