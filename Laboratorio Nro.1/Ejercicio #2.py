#Ejer. 2
class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        return(self.__a*self.__d-self.__b*self.__c)!=0
    def getX(self):
        return(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    def getY(self):
        return(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
a = float(input("ingrese a:"))
b = float(input("ingrese b:"))
c = float(input("ingrese c:"))
d = float(input("ingrese d:"))
e = float(input("ingrese e:"))
f = float(input("ingrese f:"))
eq = EcuacionLineal(a, b, c, d, e, f)
if eq.tieneSolucion():
    print("x =", eq.getX(), "y =", eq.getY())
else:
    print("La ecuacion no tiene solucion")
