#Ejer. 3
import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return self.__b**2-4*self.__a*self.__c
    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return(-self.__b+math.sqrt(d))/(2*self.__a)
        else:
            return 0
    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return(-self.__b-math.sqrt(d))/(2*self.__a)
        else:
            return 0
a = (float(input("ingrese a:")))
b = (float(input("ingrese b:")))
c = (float(input("ingrese c:")))
eq = EcuacionCuadratica(a, b, c)
d = eq.getDiscriminante()
if d > 0:
    print("La ecuacion tiene dos raices", f"{eq.getRaiz1():.6f}", "y", f"{eq.getRaiz2():.6f}")
elif d == 0:
    print("La ecuacion tiene una raiz", eq.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")
        
