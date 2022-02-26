from Organizm import Organizm
import random

class Roslina(Organizm):

    def __init__(self, polozenieX, polozenieY, swiat):
        super().__init__(polozenieX, polozenieY, swiat)
        self.inicjatywa = 0
        self.nazwaGatunku = "roslina"

    def akcja(self):
        ileProb = 0
        self.ruch(1, ileProb)


    def kolizja(self, inny):
        print(inny.nazwaGatunku, "wszedł na", self.nazwaGatunku)
        self.wojna(inny)

    def czySieRozsieje(self):
        randomowa = (random.randint(0,9))
        if randomowa == 0:
            return True
        return False