class Téglalap:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def setA(self, a):
        self.a=a
    def setB(self, b):
        self.b=b
    def setAB(self, a, b):
        self.a=a
        self.b=b
    def getA(self):
        return self.a
    def getKerulet(self):
        return 2*(self.a+self.b)
    def getTerulet(self):
        return self.a * self.b

class kocka:
    def __init__(self, a): 
        self.a=a
    def setA(self, a):
        self.a=a
    def getA(self):
        return self.a
    def getKerület(self):
        return 4*self.a
    def getTerület(self):
        return self.a*self.a

class kör:
    def __init__(self, r):
        self.r=r
    def setR(self, r):
        self.r=r
    def getR(self):
        return self.r
    def getKerület(self):
        return 2*self.r*3.14
    def getTerület(self):
        return self.r**2*3.14

class nhasáb:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def setA(self, a):
        self.a=a
    def setB(self, b):
        self.b=b
    def setC(self, c):
        self.c=c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getFelszín(self):
        return 2*((self.a*self.b)+(self.a*self.c)+(self.b*self.c))
    def getTérfogat(self):
        return self.a*self.b*self.c

class ember:
    def __init__(self, nem, név):
        self.nem=nem
        self.név=név
    def setNEM(self, nem):
        self.nem=nem
    def setNÉV(self, név):
        self.név=név
    def getNEM(self):
        return self.nem
    def getNÉV(self):
        return self.név