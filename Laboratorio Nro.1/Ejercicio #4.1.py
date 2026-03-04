#Ejer. 4.1
import math
def promedio(v):
    s = 0
    for i in range(len(v)):
        s = s + v[i]
    return s/len(v)
def desviacion(v):
    p = promedio(v)
    s = 0
    for i in range(len(v)):
        s = s + (v[i] - p)**2
    return math.sqrt(s/(len(v) - 1))
v = []
print("ingrese 10 numeros")
for i in range(10):
    n = float(input())
    v.append(n)
p = promedio(v)
d = desviacion(v)
print("El promedio es", round(p,2))
print("La desviacion estandar es", round(d,5))
