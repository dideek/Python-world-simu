from Swiat import Swiat
import pygame, sys
from button import button
pygame.init()

screen = pygame.display.set_mode((500, 500))
nowaGra = button((123, 222, 131), 150, 150, 200, 50, "Nowa gra")
wczytajGre = button((123, 222, 131), 150, 210, 200, 50, "Wczytaj grę")

while True:

    # Handle events
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (nowaGra.isOver(pos)):
                swiat = Swiat(10)
                swiat.rysujSwiat()
            if (wczytajGre.isOver(pos)):
                File = open("zapisgry.txt", "r", encoding="utf-8")
                linie = File.readlines()
                File.close()
                szerokosc = int(linie[0])
                swiat = Swiat(szerokosc, False)
                swiat.wczytajGre(linie)
                swiat.wypiszTabele()
                swiat.rysujSwiat()


    # rysowanie
    screen.fill((43, 43, 43))
    wczytajGre.draw(screen)
    nowaGra.draw(screen)
    pygame.display.flip()







