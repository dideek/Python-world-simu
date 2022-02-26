from .Roslina import Roslina
import random

class WilczeJagody(Roslina):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 99
        self.wiek = wiek
        self.color = (128, 128, 255)
        self.nazwaGatunku = "wilcze jagody"
        self.dodajDoKolejki();

    def __str__(self):
        return self.nazwaGatunku

    def akcja(self):
        if(self.czySieRozsieje()):
            x = self.polozenieX
            y = self.polozenieY
            ile_prob = 0
            while(self.czyStoiZwierze(x, y) and ile_prob < 50):
                ile_prob += 1
                randomowa = (random.randint(0,3))
                if randomowa == 0:
                    x = self.polozenieX + 1
                    y = self.polozenieY
                elif randomowa == 1:
                    x = self.polozenieX - 1
                    y = self.polozenieY
                elif randomowa == 2:
                    x = self.polozenieX
                    y = self.polozenieY + 1
                elif randomowa == 3:
                    x = self.polozenieX
                    y = self.polozenieY - 1
            if ile_prob < 50:
                print("Wilcze jagody się rozsiewają")
                guarana = WilczeJagody(x, y , self.swiat, 0)

    def kolizja(self, inny):
        print(inny.nazwaGatunku, "wszedł na Wilczą Jagodę")
        self.zabijObydwa(inny)