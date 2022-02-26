from .Zwierze import Zwierze
import random

class Zolw(Zwierze):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 2
        self.inicjatywa = 1
        self.wiek = wiek
        self.color = (0, 102, 34)
        self.nazwaGatunku = "żółw"
        self.dodajDoKolejki();

    def akcja(self):
        ilosc_prob_ruchu = 0
        if self.czySieRuszy():
            print("Żółw się rusza")
            self.ruch(1, ilosc_prob_ruchu)
        else:
            print("Żółw się nie rusza")

    def kolizja(self, atakujacy):
        if not(isinstance(atakujacy, Zolw)):
            if not(self.czySieObronil(atakujacy)):
                print("Żółw został zaatakowany przez", atakujacy.nazwaGatunku)
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
                print("Żółw się rozmnaża")
                nowywilk = Zolw(x, y, self.swiat, 0)

    def czySieRuszy(self):
        zmienna = (random.randint(0,3))
        if zmienna == 0:
            return True
        return False

    def czySieObronil(self, atakujacy):
        if atakujacy.sila < 5:
            print("Żółw obronił się przed", atakujacy.nazwaGatunku)
            return True
        print("Żółw nie obronił się przed", atakujacy.nazwaGatunku)
        return False
