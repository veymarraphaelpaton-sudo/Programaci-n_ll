#EJERCICIO 1
import random
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0
    def reiniciaPartida(self):
        print("Nueva partida")
    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas <= 0:
            print("Te quedaste sin vidas")
            return False
        else:
            print("Vidas restantes:", self.numeroDeVidas)
            return True
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = random.randint(0, 10)
    def juega(self):
        self.reiniciaPartida()
        print("Adivina un numero entre 0 y 10")
        seguir = True
        while seguir:
            n = int(input("Numero: "))
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
class Aplicacion:
    def main(self):
        juego = JuegoAdivinaNumero(3)
        juego.juega()
app = Aplicacion()
app.main()






