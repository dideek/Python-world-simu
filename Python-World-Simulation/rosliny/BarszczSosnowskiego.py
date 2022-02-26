from .Roslina import Roslina
from zwierzeta.CyberOwca import CyberOwca
import random

class BarszczSosnowskiego(Roslina):

    def __init__(self, polozenieX, polozenieY, swiat, wiek = 1):
        super().__init__(polozenieX, polozenieY, swiat)
        self.sila = 0
        self.wiek = wiek
        self.color = (255, 0, 213)
        self.nazwaGatunku = "barszcz sosnowskiego"
        self.dodajDoKolejki();

    def __str__(self):
        return self.nazwaGatunku

    def akcja(self):
        self.zabijZwierzetaDookola()
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
                print("Barszcz sosnowskiego się rozsiewa")
                guarana = BarszczSosnowskiego(x, y , self.swiat, 0)

    def kolizja(self, inny):
        print(inny.nazwaGatunku, "wszedł na Braszcz Sosnowskiego")
        if not (isinstance(inny, CyberOwca)):
            self.zabijObydwa(inny)
        else:
            print("Cyber Owca zjada Barszcz Sosnowskiego")
            x = self.polozenieX
            y = self.polozenieY
            self.umrzyj()
            inny.poruszanieSie(x, y)