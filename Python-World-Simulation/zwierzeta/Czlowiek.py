from .Zwierze import Zwierze
import random

class Czlowiek(Zwierze):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 5
        self.inicjatywa = 4
        self.wiek = wiek
        self.nazwaGatunku = "człowiek"
        self.pozostaleTury = 0
        self.color = (0,0,0)
        self.umiejetnoscAktywna = 0
        self.dodajDoKolejki();

    def __str__(self):
        return self.nazwaGatunku

    def akcja(self):
        ilosc_prob = 0
        self.tarczaAlzura();
        self.ruch(1, ilosc_prob)

    def kolizja(self, atakujacy):
        print("Zostales zaatakowany przez", atakujacy.nazwaGatunku)
        if(self.czyUmiejetnoscAktywna()):
            print("Tarcza alzura ochronila ciebie przed", atakujacy.nazwaGatunku)
            atakujacy.ucieczka(self)
        else:
            self.wojna(atakujacy)

    def czyUmiejetnoscAktywna(self):
        if(self.umiejetnoscAktywna == 0):
            return False
        return True

    def tarczaAlzura(self):
        if self.czyUmiejetnoscAktywna():
            self.pozostaleTury -= 1
            self.swiat.pozostaleTury -= 1
            if self.pozostaleTury == 0:
                self.umiejetnoscAktywna = 0
                self.swiat.umiejetnoscAktywna = 0
            else:
                print("Tarcza Alzura jest aktywna pozostaly", self.pozostaleTury)
        if not(self.czyUmiejetnoscAktywna()):
            if self.swiat.umiejetnoscAktywna == 1:
                self.umiejetnoscAktywna = 1
                self.pozostaleTury = 5
                self.swiat.pozostaleTury = 5

    def ruch(self, ileKrokow, ileProb):
        ruch = self.swiat.ruch
        if ileProb < 50:
            if ruch == 0:  # GÓRA
                self.zmienPolozenie(-ileKrokow, 0, ileProb)
            elif ruch == 1:  # DÓł
                self.zmienPolozenie(ileKrokow, 0, ileProb)
            elif ruch == 2:  # PRAWO
                self.zmienPolozenie(0, ileKrokow, ileProb)
            elif ruch == 3:  # LEWO
                self.zmienPolozenie(0, -ileKrokow, ileProb)
        

