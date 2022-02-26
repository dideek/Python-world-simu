from zwierzeta.Wilk import Wilk
from zwierzeta.Owca import Owca
from zwierzeta.Lis import Lis
from zwierzeta.Zolw import Zolw
from zwierzeta.Zwierze import Zwierze
from zwierzeta.Czlowiek import Czlowiek
from zwierzeta.Antylopa import Antylopa
from rosliny.Trawa import Trawa
from rosliny.Mlecz import Mlecz
from rosliny.Guarana import Guarana
from rosliny.WilczeJagody import WilczeJagody
from rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from zwierzeta.CyberOwca import CyberOwca
from button import button
import pygame, sys
import random

class Swiat:

    def __init__(self, szerokosc, czyNowy = True):
        self.szerokosc = szerokosc
        self.tura = 1
        self.pozostaleTury = 0
        self.ruch = 0
        self.umiejetnoscAktywna = 0
        self.__kolejkaOrganizmow = []
        self.__tabelaOrganizmow = []
        self.stworzTabele()
        if czyNowy:
            self.dodajPoczatekZwierzat()


    def pokazszerokosc(self):
        print("Szerokość " + str(self.szerokosc))

    def dodajOrganizmDoKolejki(self, organizm):
        self.__kolejkaOrganizmow.append(organizm)
        self.__kolejkaOrganizmow.sort(key=lambda x:( x.inicjatywa, x.wiek), reverse=True)



    def dodajOrganizmDoTabeli(self,zwierze, polozenieX, polozenieY):
        self.__tabelaOrganizmow[polozenieX][polozenieY] = zwierze

    def wypiszOrganizmy(self):
        for i in self.__kolejkaOrganizmow:
            i.pokazDane()

    def stworzTabele(self):
        self.__tabelaOrganizmow = [[None for x in range(self.szerokosc)] for y in range(self.szerokosc)]
        for a in range(self.szerokosc):
            for b in range(self.szerokosc):
                self.__tabelaOrganizmow[a][b]= None

    def wypiszTabele(self):
        for a in range(self.szerokosc):
            print (str(self.__tabelaOrganizmow[a]))
            print("")

    def dodajPoczatekZwierzat(self):
        Zolw(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Zolw(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Wilk(random.randint(0, self.szerokosc-1), random.randint(0, self.szerokosc-1), self)
        Wilk(random.randint(0, self.szerokosc-1), random.randint(0, self.szerokosc-1), self)
        Czlowiek(random.randint(0, self.szerokosc-1), random.randint(0, self.szerokosc-1), self)
        Owca(random.randint(0, self.szerokosc-1), random.randint(0, self.szerokosc-1), self)
        Owca(random.randint(0, self.szerokosc-1), random.randint(0, self.szerokosc-1), self)
        BarszczSosnowskiego(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        BarszczSosnowskiego(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        CyberOwca(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Antylopa(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Antylopa(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Trawa(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Mlecz(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Lis(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Lis(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        WilczeJagody(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)
        Guarana(random.randint(0, self.szerokosc - 1), random.randint(0, self.szerokosc - 1), self)

    def poruszZwierzeciem(self, stareX, stareY, noweX, noweY):
        self.__tabelaOrganizmow[noweX][noweY] = self.__tabelaOrganizmow[stareX][stareY]
        self.__tabelaOrganizmow[stareX][stareY] = None

    def czyWychodziPozaSwiat(self, x, y):
        if (x >= self.szerokosc or x < 0 or y < 0 or y >= self.szerokosc):
            return True
        return False

    def czyZajete(self, x, y):
        if (not(self.czyWychodziPozaSwiat(x, y))):
            if (self.__tabelaOrganizmow[x][y] != None):
                return True
            return False
        return True

    def getZwierzeZTablicy(self, x, y):
        return self.__tabelaOrganizmow[x][y]

    def wykonajTure(self):
        print("Autor: Jan Jetke")
        print("Indeks: 180278 (Umiejetnosc - Tarcza Alzura)")
        print("Poczatek tury:", self.tura)
        self.wypiszOrganizmy()
        for organizm in self.__kolejkaOrganizmow:
            organizm.wiek += 1
            if organizm.wiek > 1:
                organizm.akcja()
        self.wypiszTabele()
        self.tura += 1

    def WALKA(self, broniacy, atakujacy):
        if atakujacy.sila >= broniacy.sila:
            x = broniacy.polozenieX
            y = broniacy.polozenieY
            self.usunZeSwiata(broniacy)
            atakujacy.poruszanieSie(x,y)
        elif atakujacy.sila < broniacy.sila:
            self.usunZeSwiata(atakujacy)

    def usunZeSwiata(self, organizm):
        self.__tabelaOrganizmow[organizm.polozenieX][organizm.polozenieY] = None
        self.usunZTabeli(organizm)

    def usunZTabeli(self, organizm):
        i = 0
        for x in self.__kolejkaOrganizmow:
            if x == organizm:
                print(organizm.nazwaGatunku, "umiera")
                del self.__kolejkaOrganizmow[i]
            i += 1

    def ucieczka(self, uciekajacy, atakujacy):
        x = uciekajacy.polozenieX
        y = uciekajacy.polozenieY
        nx = x
        ny = y
        ilosc_prob = 0
        while uciekajacy.czyStoiZwierze(x, y) and ilosc_prob < 50:
            i = (random.randint(0, 3))
            ilosc_prob += 1
            if i == 0:
                x = uciekajacy.polozenieX + 1
                y = uciekajacy.polozenieY
            elif i == 1:
                x = uciekajacy.polozenieX - 1
                y = uciekajacy.polozenieY
            elif i == 2:
                x = uciekajacy.polozenieX
                y = uciekajacy.polozenieY + 1
            elif i == 3:
                x = uciekajacy.polozenieX
                y = uciekajacy.polozenieY - 1
        uciekajacy.poruszanieSie(x, y)
        atakujacy.poruszanieSie(nx, ny)

    def zabijOba(self, pierwszy, drugi):
        self.usunZeSwiata(pierwszy)
        self.usunZeSwiata(drugi)

    def zabijZwierzetaDookola(self, organizm):
        x = organizm.polozenieX
        y = organizm.polozenieY
        if self.czyStoiZwierze(x+1, y):
            if not(isinstance(self.getZwierzeZTablicy(x+1, y), CyberOwca)):
                print("Barszcz rozsiewa trująca chmure")
                self.usunZeSwiata(self.getZwierzeZTablicy(x+1, y))
        if self.czyStoiZwierze(x-1, y):
            if not(isinstance(self.getZwierzeZTablicy(x - 1, y), CyberOwca)):
                print("Barszcz rozsiewa trująca chmure")
                self.usunZeSwiata(self.getZwierzeZTablicy(x-1, y))
        if self.czyStoiZwierze(x, y+1):
            if not (isinstance(self.getZwierzeZTablicy(x, y+1), CyberOwca)):
                print("Barszcz rozsiewa trująca chmure")
                self.usunZeSwiata(self.getZwierzeZTablicy(x, y+1))
        if self.czyStoiZwierze(x, y-1):
            if not (isinstance(self.getZwierzeZTablicy(x, y-1), CyberOwca)):
                print("Barszcz rozsiewa trująca chmure")
                self.usunZeSwiata(self.getZwierzeZTablicy(x, y-1))

    def czyStoiZwierze(self, x, y):
        if not(self.czyWychodziPozaSwiat(x, y)):
            if self.czyZwierze(x, y):
                return True
        return False

    def czyZwierze(self, x, y):
        if isinstance(self.getZwierzeZTablicy(x, y), Zwierze):
            return True
        return False

    def zapiszStanGry(self):
        File = open("zapisgry.txt", "w", encoding="utf-8")
        File.write(str(self.szerokosc) + "\n")
        File.write(str(self.tura) + "\n")
        for x in self.__kolejkaOrganizmow:
            if not(isinstance(x, Czlowiek)):
                File.write(str(x.nazwaGatunku) + "\n")
                File.write(str(x.polozenieX) + "\n")
                File.write(str(x.polozenieY) + "\n")
                File.write(str(x.sila) + "\n")
                File.write(str(x.inicjatywa) + "\n")
                File.write(str(x.wiek) + "\n")
            else:
                File.write(str(x.nazwaGatunku) + "\n")
                File.write(str(x.polozenieX) + "\n")
                File.write(str(x.polozenieY) + "\n")
                File.write(str(x.sila) + "\n")
                File.write(str(x.inicjatywa) + "\n")
                File.write(str(x.wiek) + "\n")
                File.write(str(x.umiejetnoscAktywna) + "\n")
                File.write(str(x.pozostaleTury) + "\n")

        File.close()

    def wczytajGre(self, linie):
        self.szerokosc = int(linie.pop(0))
        self.tura = int(linie.pop(0))
        while len(linie) > 0:
            nazwaGatunku = linie.pop(0).replace("\n", "")
            polozenieX = int(linie.pop(0))
            polozenieY = int(linie.pop(0))
            sila = int(linie.pop(0))
            inicjatywa = int(linie.pop(0))
            wiek = int(linie.pop(0))
            if nazwaGatunku == "wilk":
                Wilk(polozenieX, polozenieY, self)
                Wilk.nazwaGatunku = nazwaGatunku
                Wilk.sila = sila
                Wilk.inicjatywa = inicjatywa
                Wilk.wiek = wiek
            elif nazwaGatunku == "owca":
                Owca(polozenieX, polozenieY, self)
                Owca.nazwaGatunku = nazwaGatunku
                Owca.sila = sila
                Owca.inicjatywa = inicjatywa
                Owca.wiek = wiek
            elif nazwaGatunku == "żółw":
                Zolw(polozenieX, polozenieY, self)
                Zolw.nazwaGatunku = nazwaGatunku
                Zolw.sila = sila
                Zolw.inicjatywa = inicjatywa
                Zolw.wiek = wiek
            elif nazwaGatunku == "antylopa":
                Antylopa(polozenieX, polozenieY, self)
                Antylopa.nazwaGatunku = nazwaGatunku
                Antylopa.sila = sila
                Antylopa.inicjatywa = inicjatywa
                Antylopa.wiek = wiek
            elif nazwaGatunku == "lis":
                Lis(polozenieX, polozenieY, self)
                Lis.nazwaGatunku = nazwaGatunku
                Lis.sila = sila
                Lis.inicjatywa = inicjatywa
                Lis.wiek = wiek
            elif nazwaGatunku == "trawa":
                Trawa(polozenieX, polozenieY, self)
                Trawa.nazwaGatunku = nazwaGatunku
                Trawa.sila = sila
                Trawa.inicjatywa = inicjatywa
                Trawa.wiek = wiek
            elif nazwaGatunku == "mlecz":
                Mlecz(polozenieX, polozenieY, self)
                Mlecz.nazwaGatunku = nazwaGatunku
                Mlecz.sila = sila
                Mlecz.inicjatywa = inicjatywa
                Mlecz.wiek = wiek
            elif nazwaGatunku == "guarana":
                Guarana(polozenieX, polozenieY, self)
                Guarana.nazwaGatunku = nazwaGatunku
                Guarana.sila = sila
                Guarana.inicjatywa = inicjatywa
                Guarana.wiek = wiek
            elif nazwaGatunku == "wilcze jagody":
                WilczeJagody(polozenieX, polozenieY, self)
                WilczeJagody.nazwaGatunku = nazwaGatunku
                WilczeJagody.sila = sila
                WilczeJagody.inicjatywa = inicjatywa
                WilczeJagody.wiek = wiek
            elif nazwaGatunku == "barszcz sosnowskiego":
                BarszczSosnowskiego(polozenieX, polozenieY, self)
                BarszczSosnowskiego.nazwaGatunku = nazwaGatunku
                BarszczSosnowskiego.sila = sila
                BarszczSosnowskiego.inicjatywa = inicjatywa
                BarszczSosnowskiego.wiek = wiek
            elif nazwaGatunku == "człowiek":
                czyAktywna = wiek = int(linie.pop(0))
                pozostaleTury = int(linie.pop(0))
                Czlowiek(polozenieX, polozenieY, self)
                Czlowiek.nazwaGatunku = nazwaGatunku
                Czlowiek.sila = sila
                Czlowiek.inicjatywa = inicjatywa
                Czlowiek.wiek = wiek
                Czlowiek.umiejetnoscAktywna = czyAktywna
                self.umiejetnoscAktywna = czyAktywna
                self.pozostaleTury = pozostaleTury
                Czlowiek.pozostaleTury = pozostaleTury
            elif nazwaGatunku == "cyber owca":
                CyberOwca(polozenieX, polozenieY, self)
                CyberOwca.nazwaGatunku = nazwaGatunku
                CyberOwca.sila = sila
                CyberOwca.inicjatywa = inicjatywa
                CyberOwca.wiek = wiek

    def wybierzBarszcz(self, owca):
        x = owca.polozenieX
        y = owca.polozenieY
        suma = self.szerokosc*2
        barszcz = None
        for organizm in self.__kolejkaOrganizmow:
            if isinstance(organizm, BarszczSosnowskiego):
                if (abs(organizm.polozenieX-x) + abs(organizm.polozenieY-y)) < suma:
                    suma = (abs(organizm.polozenieX-x) + abs(organizm.polozenieY-y))
                    barszcz = organizm
        return barszcz

    def rysujSwiat(self):
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        box = pygame.Rect(10,10,50,50)
        nastepnaTura = button((123, 222, 131), 700, 10, 200, 50, "Następna Tura")
        aktywujUmiejetnosc = button((123, 222, 131), 700, 70, 200, 50, "Aktywuj Tarcze")
        clock = pygame.time.Clock()
        while True:
            pygame.init()
            screen = pygame.display.set_mode((1280, 720))
            box = pygame.Rect(10, 10, 50, 50)
            nastepnaTura = button((123, 222, 131), 700, 10, 200, 50, "Następna Tura")
            zapiszGre = button((123, 222, 131), 700, 130, 200, 50, "Zapisz grę")
            aktywujUmiejetnosc = button((123, 222, 131), 700, 70, 200, 50, "Aktywuj Tarcze")
            umiejetnoscAktywna = button((123, 222, 131), 700, 70, 200, 50, "Tarcza aktywna: " + str(self.pozostaleTury))
            clock.tick(30)
            #Handle events
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(nastepnaTura.isOver(pos)):
                        print("dupa")
                        self.wykonajTure()
                    if (aktywujUmiejetnosc.isOver(pos)):
                        print("aktywuj umiejetnosc")
                        self.umiejetnoscAktywna = 1
                        if(self.pozostaleTury == 0):
                            self.pozostaleTury = 5
                    if (zapiszGre.isOver(pos)):
                        print("Zapisuje grę")
                        self.zapiszStanGry()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                print("Góra")
                self.ruch = 0
                self.wykonajTure()
            if keys[pygame.K_DOWN]:
                print("Dół")
                self.ruch = 1
                self.wykonajTure()
            if keys[pygame.K_RIGHT]:
                print("Prawo")
                self.ruch = 2
                self.wykonajTure()
            if keys[pygame.K_LEFT]:
                print("Lewo")
                self.ruch = 3
                self.wykonajTure()


            #input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                box.x += 1
            if keys[pygame.K_s]:
                box.y += 1
            if keys[pygame.K_a]:
                box.x -= 1
            if keys[pygame.K_w]:
                box.y -= 1


            #rysowanie
            screen.fill((43,43,43))
            self.rysujTabele(screen)
            nastepnaTura.draw(screen)
            if self.umiejetnoscAktywna == 0:
                aktywujUmiejetnosc.draw(screen)
            else:
                umiejetnoscAktywna.draw(screen)
            zapiszGre.draw(screen)
            self.rysujLegende(screen)
            pygame.display.flip()


    def rysujTabele(self, screen):
        box = pygame.Rect(10, 10, 50, 50)
        pygame.draw.rect(screen,(220,220,220) , pygame.Rect(0, 0, 610, 610) )
        RED = (50, 120, 120)
        for x in range(self.szerokosc):
            box.y = 10
            for y in range(self.szerokosc):
                if self.__tabelaOrganizmow[y][x] != None:
                    pygame.draw.rect(screen, self.__tabelaOrganizmow[y][x].color, box)
                else:
                    pygame.draw.rect(screen, RED, box)
                box.y += 60
            box.x += 60

    def rysujLegende(self,screen):
        box = pygame.Rect(10, 10, 50, 50)
        GRACZ = button((128, 255, 128), 700, 190, 100, 100, "trawa")
        GRACZ.draw(screen)
        ANTYLOPA = button((255, 191, 128), 700, 300, 100, 100, "antylopa")
        ANTYLOPA.draw(screen)
        MLECZ = button((230, 230, 0), 700, 410, 100, 100, "mlecz")
        MLECZ.draw(screen)
        BARSZCZ = button((255, 0, 213), 700, 520, 100, 100, "barszcz")
        BARSZCZ.draw(screen)
        JAGODY = button((128, 128, 255), 810, 190, 100, 100, "jagody")
        JAGODY.draw(screen)
        GUARANA = button((204, 0, 0), 810, 300, 100, 100, "guarana")
        GUARANA.draw(screen)
        CYBER = button((80, 80, 80), 810, 410, 100, 100, "CYBER")
        CYBER.draw(screen)
        LIS = button((230, 82, 0), 810, 520, 100, 100, "lis")
        LIS.draw(screen)
        OWCA = button((255, 255, 255), 920, 190, 100, 100, "owca")
        OWCA.draw(screen)
        WILK = button((128, 128, 128), 920, 300, 100, 100, "wilk")
        WILK.draw(screen)
        ZOLW = button( (0, 102, 34), 920, 410, 100, 100, "żółw")
        ZOLW.draw(screen)
        GRACZ = button((0,0,0), 920, 520, 100, 100, "gracz")
        GRACZ.draw(screen)
