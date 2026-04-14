#EJERCICIO 2
import random
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0
    def reiniciaPartida(self):
        print("\nNueva partida")
    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas <= 0:
            print("Sin vidas")
            return False
        else:
            print("Vidas:", self.numeroDeVidas)
            return True
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = random.randint(0, 10)
    def validaNumero(self, n):
        if 0 <= n <= 10:
            return True
        else:
            print("Numero fuera de rango")
            return False
    def juega(self):
        self.reiniciaPartida()
        print("Adivina un numero entre 0 y 10")
        seguir = True
        while seguir:
            n = int(input("Numero: "))
            if not self.validaNumero(n):
                continue
            if n == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if n < self.numeroAAdivinar:
                    print("Es mayor")
                else:
                    print("Es menor")
                seguir = self.quitaVida()
        if not seguir:
            print("Perdiste")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10:
            if n % 2 == 0:
                return True
            else:
                print("Error: el numero debe ser PAR")
                return False
        else:
            print("Numero fuera de rango")
            return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10:
            if n % 2 != 0:
                return True
            else:
                print("Error: el numero debe ser IMPAR")
                return False
        else:
            print("Numero fuera de rango")
            return False
class Aplicacion:
    def main(self):
        j1 = JuegoAdivinaNumero(3)
        j2 = JuegoAdivinaPar(3)
        j3 = JuegoAdivinaImpar(3)
        print("\n--- Juego normal ---")
        j1.juega()
        print("\n--- Juego PAR ---")
        j2.juega()
        print("\n--- Juego IMPAR ---")
        j3.juega()
app = Aplicacion()
app.main()



