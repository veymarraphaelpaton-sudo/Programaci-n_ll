#EJERCICIO 3
import math
class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def __add__(self, b):
        return Vector3D(
            self.a1 + b.a1,
            self.a2 + b.a2,
            self.a3 + b.a3
        )
    def __mul__(self, r):
        return Vector3D(
            r * self.a1,
            r * self.a2,
            r * self.a3
        )
    def longitud(self):
        return math.sqrt(
            self.a1**2 +
            self.a2**2 +
            self.a3**2
        )
    def normal(self):
        l = self.longitud()
        return Vector3D(
            self.a1/l,
            self.a2/l,
            self.a3/l
        )
    def producto_escalar(self, b):
        return (
            self.a1*b.a1 +
            self.a2*b.a2 +
            self.a3*b.a3
        )
    def producto_vectorial(self, b):
        return Vector3D(
            self.a2*b.a3 - self.a3*b.a2,
            self.a3*b.a1 - self.a1*b.a3,
            self.a1*b.a2 - self.a2*b.a1
        )
    def mostrar(self):
        print(f"({self.a1}, {self.a2}, {self.a3})")
a = Vector3D(1,2,3)
b = Vector3D(4,5,6)
print("Suma de vectores:")
c = a + b
c.mostrar()
print("Multiplicación por escalar:")
d = a * 2
d.mostrar()
print("Longitud de a:")
print(a.longitud())
print("Vector normal de a:")
n = a.normal()
n.mostrar()
print("Producto escalar:")
print(a.producto_escalar(b))
print("Producto vectorial:")
pv = a.producto_vectorial(b)








pv.mostrar()
