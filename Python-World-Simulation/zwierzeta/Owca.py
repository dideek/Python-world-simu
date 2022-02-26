from .Zwierze import Zwierze
import random

class Owca(Zwierze):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 4
        self.inicjatywa = 4
        self.wiek = wiek
        self.color = (255, 255, 255)
        self.nazwaGatunku = "owca"
        self.dodajDoKolejki();

    def kolizja(self, atakujacy):
        if not(isinstance(atakujacy, Owca)):
            print("Owca został zaatakowany przez", atakujacy.nazwaGatunku)
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
                print("Owca się rozmnaża")
                nowaowca = Owca(x, y, self.swiat, 0)
