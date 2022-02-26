from .Zwierze import Zwierze
import random

class CyberOwca(Zwierze):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 11
        self.inicjatywa = 4
        self.wiek = wiek
        self.color = (80, 80, 80)
        self.nazwaGatunku = "cyber owca"
        self.dodajDoKolejki();
        self.wybranyBarszcz = None

    def kolizja(self, atakujacy):
        if not(isinstance(atakujacy, CyberOwca)):
            print("Cyber owca została zaatakowana przez", atakujacy.nazwaGatunku)
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
                print("Cyber owca się rozmnaża")
                nowaowca = CyberOwca(x, y, self.swiat, 0)

    def akcja(self):
        self.wybranyBarszcz = self.wybierzNajblizszyBarszcz()
        ileProb = 0
        self.ruch(1, ileProb)

    def ruch(self, ileKrokow, ileProb):
        if self.wybranyBarszcz != None:
            if ileProb < 50:
                if (self.polozenieX - self.wybranyBarszcz.polozenieX) > 0:  # GÓRA
                    self.zmienPolozenie(-ileKrokow, 0, ileProb)
                elif (self.polozenieX - self.wybranyBarszcz.polozenieX) < 0 :  # DÓł
                    self.zmienPolozenie(ileKrokow, 0, ileProb)
                elif (self.polozenieY - self.wybranyBarszcz.polozenieY) < 0:  # PRAWO
                    self.zmienPolozenie(0, ileKrokow, ileProb)
                elif (self.polozenieY - self.wybranyBarszcz.polozenieY) > 0:  # LEWO
                    self.zmienPolozenie(0, -ileKrokow, ileProb)
        else:
            ruch = (random.randint(0, 3))
            if ileProb < 50:
                if ruch == 0:  # GÓRA
                    self.zmienPolozenie(-ileKrokow, 0, ileProb)
                elif ruch == 1:  # DÓł
                    self.zmienPolozenie(ileKrokow, 0, ileProb)
                elif ruch == 2:  # PRAWO
                    self.zmienPolozenie(0, ileKrokow, ileProb)
                elif ruch == 3:  # LEWO
                    self.zmienPolozenie(0, -ileKrokow, ileProb)

