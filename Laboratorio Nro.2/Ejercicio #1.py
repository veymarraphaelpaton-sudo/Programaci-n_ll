#EJERCICIO 1
import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, p):
        return math.sqrt((self.__x - p.getX())**2 + (self.__y - p.getY())**2)
    def distancia__xy(self, x, y):
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
print("Distancia entre los puntos", p1.distancia(p2))
