from .Zwierze import Zwierze
import random

class Lis(Zwierze):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 3
        self.inicjatywa = 7
        self.wiek = wiek
        self.color = (230, 82, 0)
        self.nazwaGatunku = "lis"
        self.dodajDoKolejki();

    def kolizja(self, atakujacy):
        if not(isinstance(atakujacy, Lis)):
            print("Lis został zaatakowany przez", atakujacy.nazwaGatunku)
            self.wojna(atakujacy)
        else:
            x = self.polozenieX
            y = self.polozenieY
            ilosc_prob = 0
            while (self.czyStoiZwierze(x, y) and ilosc_prob < 50):
                i = (random.randint(0,7))
                ilosc_prob += 1
                if i == 0:
                    x = self.polozenieX + 1
                    y = self.polozenieY
                elif i == 1:
                    x = self.polozenieX - 1
                    y = self.polozenieY
                elif i == 2:
                    x = self.polozenieX
                    y = self.polozenieY + 1
                elif i == 3:
                    x = self.polozenieX
                    y = self.polozenieY - 1
                elif i == 4:
                    x = atakujacy.polozenieX + 1
                    y = atakujacy.polozenieY
                elif i == 5:
                    x = atakujacy.polozenieX - 1
                    y = atakujacy.polozenieY
                elif i == 6:
                    x = atakujacy.polozenieX
                    y = atakujacy.polozenieY + 1
                elif i == 7:
                    x = atakujacy.polozenieX
                    y = atakujacy.polozenieY - 1
            if ilosc_prob < 50:
                print("Lis się rozmnaża")
                nowylis = Lis(x, y, self.swiat, 0)

    def zmienPolozenie(self, x, y, ileProb):
        nx = self.polozenieX + x
        ny = self.polozenieY + y
        if (self.czyWychodziPozaTablice(nx, ny)):
            ileProb += 1
            self.ruch(1, ileProb)
        else:
            if (self.czyStoiZwierze(nx, ny)):
                if(self.naCoWszedl(nx, ny).sila > self.sila):
                    self.ruch(1, ileProb)
                else:
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
                self.poruszanieSie(nx, ny)
