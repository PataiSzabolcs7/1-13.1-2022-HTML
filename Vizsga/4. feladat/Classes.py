class Menetlevél():
    def __init__(self, rendszám, megtett, fogyasztás):
        self.rendszám = rendszám
        self.megtett = megtett
        self.fogyasztás = fogyasztás
    def setREND(self, rendszám):
        self.rendszám=rendszám
    def setMEG(self, megtett):
        self.megtett=megtett
    def setFOGY(self, fogyasztás):
        self.fogyasztás=fogyasztás
    def getREND(self):
        return self.rendszám
    def getMEG(self):
        return self.megtett
    def getFOGY(self):
        return self.fogyasztás