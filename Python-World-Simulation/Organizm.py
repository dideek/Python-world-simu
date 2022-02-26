from abc import ABC, abstractmethod
import random

class Organizm(ABC):

    def __init__(self, polozenieX, polozenieY, swiat):
        self.swiat = swiat
        self.polozenieX = polozenieX
        self.polozenieY = polozenieY
        while self.swiat.czyZajete(self.polozenieX, self.polozenieY):
            self.polozenieX = (random.randint(0, self.swiat.szerokosc-1))
            self.polozenieY = (random.randint(0, self.swiat.szerokosc-1))
        self.nazwaGatunku = "-"
        self.inicjatywa = 0
        self.wiek = 0
        self.swiat.dodajOrganizmDoTabeli(self, polozenieX, polozenieY)

    def __str__(self):
        return self.nazwaGatunku

    def __gt__(self, inny):
        if self.inicjatywa >= inny.inicjatywa:
            return self
        elif self.inicjatywa < inny.inicjatywa:
            return inny
        else:
            if self.wiek > inny.wiek:
                return self
            else:
                return inny

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self):
        pass

    def dodajDoKolejki(self):
        self.swiat.dodajOrganizmDoKolejki(self);

    def poruszanieSie(self, x, y):
        self.swiat.poruszZwierzeciem(self.polozenieX, self.polozenieY, x, y)
        self.polozenieX = x
        self.polozenieY = y

    def czyWychodziPozaTablice(self, x, y):
        return self.swiat.czyWychodziPozaSwiat(x, y)

    def czyStoiZwierze(self, x, y):
        return self.swiat.czyZajete(x, y)

    def naCoWszedl(self, x, y):
        return self.swiat.getZwierzeZTablicy(x, y)

    def pokazDane(self):
        print("Organizm " + self.nazwaGatunku + ", inicjatywa: " + str(self.inicjatywa) + ", sila: " + str(self.sila) + ", wiek: "+ str(self.wiek) + ", pozycja (x,y): (" + str(self.polozenieX) + ", " + str(self.polozenieY) + ")")

    def wojna(self, atakujacy):
        self.swiat.WALKA(self, atakujacy)

    def ucieczka(self, atakujacy):
        self.swiat.ucieczka(self, atakujacy)

    def zabijObydwa(self, inny):
        self.swiat.zabijOba(self, inny)

    def zabijZwierzetaDookola(self):
        self.swiat.zabijZwierzetaDookola(self)

    def wybierzNajblizszyBarszcz(self):
        return self.swiat.wybierzBarszcz(self)

    def umrzyj(self):
        self.swiat.usunZeSwiata(self)