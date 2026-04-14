#EJERCICIO 2
import math
class AlgebraVectorial:
    def __init__(self, a1=0, a2=0, b1=0, b2=0):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
    def producto_punto(self):
        return self.a1*self.b1 + self.a2*self.b2
    def norma(self, x, y):
        return math.sqrt(x**2 + y**2)
    def perpendicular1(self):
        apd = self.norma(self.a1+self.b1, self.a2+self.b2)
        amb = self.norma(self.a1-self.b1, self.a2-self.b2)
        return apd == amb
    def perpendicular2(self):
        amb = self.norma(self.a1-self.b1, self.a2-self.b2)
        bma = self.norma(self.b1-self.a1, self.b2-self.a2)
        return amb == bma
    def perpendicular3(self):
        return self.producto_punto()==0
    def perpendicular4(self):
        apd = self.norma(self.a1+self.b1, self.a2+self.b2)**2
        na = self.norma(self.a1, self.a2)**2
        nb = self.norma(self.b1, self.b2)**2
        return apd == na + nb
    def paralela1(self):
        if self.b1 != 0:
            r = self.a1/self.b1
            return self.a2 == r*self.b2
        return False
    def paralela2(self):
        return self.a1*self.b2 - self.a2*self.b1 == 0
    def proyeccion(self):
        punto = self.producto_punto()
        nb = self.norma(self.b1, self.b2)**2
        k = punto/nb
        return (k*self.b1, k*self.b2)
    def componente(self):
        punto = self.producto_punto()
        nb = self.norma(self.b1, self.b2)
        return punto/nb
v = AlgebraVectorial(2, 3, 4, 5)
print("Perpendicular (forma1):", v.perpendicular1())
print("Perpendicular (forma2):", v.perpendicular2())
print("Perpendicular (forma3):", v.perpendicular3())
print("Perpendicular (forma4):", v.perpendicular4())
print("Paralela (forma 1):", v.paralela1())
print("Paralela (forma 2):", v.paralela2())
print("Proyeccion de a sobre b:", v.proyeccion())
print("Componente de a en b:", v.componente())




