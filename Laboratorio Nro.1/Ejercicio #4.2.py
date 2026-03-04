#Ejer. 4.2
import math
class Estadistica:
    def __init__(self, datos):
        self.__datos = datos
    def promedio(self):
        s = 0
        for i in range(len(self.__datos)):
            s = s + self.__datos[i]
        return s/len(self.__datos)
    def desviacion(self):
        p = self.promedio()
        s = 0
        for i in range(len(self.__datos)):
            s = s + (self.__datos[i] - p)**2
        return math.sqrt(s/(len(self.__datos) - 1))
v = []
print("ingrese 10 numeros")
for i in range(10):
    n = float(input())
    v.append(n)
e = Estadistica(v)
print("El promedio es", round(e.promedio(), 2))
print("La desviacion estandar es", round(e.desviacion(), 5))
