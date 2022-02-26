from Organizm import Organizm
import random

class Zwierze(Organizm):

    def __init__(self, polozenieX, polozenieY, swiat):
        super().__init__(polozenieX, polozenieY, swiat)
        self.nazwaGatunku = "Zwierze"

    def akcja(self):
        ileProb = 0
        self.ruch(1, ileProb)


    def kolizja(self, inny):
        print(self.wyp)

    def ruch(self, ileKrokow, ileProb):
        ruch = (random.randint(0,3))
        if ileProb < 50:
            if ruch == 0: #GÓRA
                self.zmienPolozenie(-ileKrokow, 0, ileProb)
            elif ruch == 1: #DÓł
                self.zmienPolozenie(ileKrokow, 0, ileProb)
            elif ruch == 2: #PRAWO
                self.zmienPolozenie(0, ileKrokow, ileProb)
            elif ruch == 3: #LEWO
                self.zmienPolozenie(0, -ileKrokow, ileProb)

    def zmienPolozenie(self, x, y, ileProb):
        nx = self.polozenieX + x
        ny = self.polozenieY + y
        if (self.czyWychodziPozaTablice(nx, ny)):
            ileProb += 1
            self.ruch(1, ileProb)
        else:
            if (self.czyStoiZwierze(nx, ny)):
                self.naCoWszedl(nx, ny).kolizja(self)
            else:
                if (x < 0):
                    print(self.nazwaGatunku + " porusza się w górę")
                elif (x > 0):
                    print(self.nazwaGatunku + " porusza się w dół")
                elif (y > 0):
                    print(self.nazwaGatunku + " porusza się w prawo")
                elif (y < 0):
                    print(self.nazwaGatunku + " porusza się w lewo")
                self.poruszanieSie(nx,ny)



