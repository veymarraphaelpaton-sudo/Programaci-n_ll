#Ejercicio 1
import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = 0
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return(self.__finaliza-self.__inicia)*1000
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
def seleccion(v):
    n = len(v)
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if v[j] < v[pos]:
                pos = j
        aux = v[i]
        v[i] = v[pos]
        v[pos] = aux
v = []
for i in range(100000):
    v.append(random.randint(1, 100000))
c = Cronometro()
c.inicia()
seleccion(v)
c.detener()
print("Tiempo en Milisegundos:", c.lapsoDeTiempo())
