import random
from tkinter import *
from Organizm import Organizm
from Polozenie import Polozenie
from Zwierzeta.Czlowiek import Czlowiek
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.Cyberowca import Cyberowca
from Zwierzeta.Lis import Lis
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Zolw import Zolw
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody

class Swiat:
    _wysokosc = 20
    _szerokosc = 20
    _liczbaSasiednichPol = 4
    _statusCzlowieka = False
    czlowiek = None
    tablicaOrganizmow = []
    organizmy = []
    plansza = None

    def __init__(self, plansza):
        self._statusCzlowieka = True
        self.plansza = plansza
        for i in range(0, self._wysokosc):
            wiersz = []
            for j in range(0, self._szerokosc):
                wiersz.append(None)
            self.tablicaOrganizmow.append(wiersz)
        self.zaludnianie()

    def losujPolozenie(self):
        while True:
            x = random.randint(0, self._szerokosc - 1)
            y = random.randint(0, self._wysokosc - 1)
            if self.tablicaOrganizmow[y][x] is None:
                return Polozenie(x, y)

    def dodajOrganizm(self, organizm: Organizm):
        self.organizmy.append(organizm)
        self.tablicaOrganizmow[organizm.polozenie.y][organizm.polozenie.x] = organizm

    def zaludnianie(self):
        polozenieCzlowieka = Polozenie(19, 9)
        self.czlowiek = Czlowiek(self, polozenieCzlowieka, 4, 0, 5, 5, 0)
        self.dodajOrganizm(self.czlowiek)

        self.dodajOrganizm(Antylopa(self, self.losujPolozenie(), 4, 0, 4))
        self.dodajOrganizm(Antylopa(self, self.losujPolozenie(), 4, 0, 4))

        self.dodajOrganizm(BarszczSosnowskiego(self, self.losujPolozenie(), 0, 0, 10))
        self.dodajOrganizm(BarszczSosnowskiego(self, self.losujPolozenie(), 0, 0, 10))

        self.dodajOrganizm(Cyberowca(self, self.losujPolozenie(), 4, 0, 11))
        self.dodajOrganizm(Cyberowca(self, self.losujPolozenie(), 4, 0, 11))

        self.dodajOrganizm(Guarana(self, self.losujPolozenie(), 0, 0, 0))
        self.dodajOrganizm(Guarana(self, self.losujPolozenie(), 0, 0, 0))

        self.dodajOrganizm(Lis(self, self.losujPolozenie(), 7, 0, 3))
        self.dodajOrganizm(Lis(self, self.losujPolozenie(), 7, 0, 3))

        self.dodajOrganizm(Mlecz(self, self.losujPolozenie(), 0, 0, 0))
        self.dodajOrganizm(Mlecz(self, self.losujPolozenie(), 0, 0, 0))

        self.dodajOrganizm(Owca(self, self.losujPolozenie(), 4, 0, 4))
        self.dodajOrganizm(Owca(self, self.losujPolozenie(), 4, 0, 4))

        self.dodajOrganizm(Trawa(self, self.losujPolozenie(), 0, 0, 0))
        self.dodajOrganizm(Trawa(self, self.losujPolozenie(), 0, 0, 0))

        self.dodajOrganizm(WilczeJagody(self, self.losujPolozenie(), 0, 0, 99))
        self.dodajOrganizm(WilczeJagody(self, self.losujPolozenie(), 0, 0, 99))

        self.dodajOrganizm(Wilk(self, self.losujPolozenie(), 5, 0, 9))
        self.dodajOrganizm(Wilk(self, self.losujPolozenie(), 5, 0, 9))

        self.dodajOrganizm(Zolw(self, self.losujPolozenie(), 1, 0, 2))
        self.dodajOrganizm(Zolw(self, self.losujPolozenie(), 1, 0, 2))

    def sortuj(self):
        self.organizmy.sort(key=lambda organizm: int(organizm.getInicjatywa()), reverse=True)

    def wykonajTure(self):
        self.sortuj()
        if self.czlowiek.getCzyZywy():
            for i in self.organizmy:
                if i.getCzyZywy():
                    i.akcja()
                    i.setWiek(int(i.getWiek()) + 1)
            self.plansza.panelGry.delete("all")
            self.plansza.rysujSwiat()
        else:
            self.plansza.komentator.insert('end', "Czlowiek umarl, koniec gry!")
            return

    def zapisz(self):
        oknoDialogowe = Tk()
        tekst = Entry(oknoDialogowe)
        tekst.pack()

        def potwiedzZapis():
            nazwaPliku = tekst.get()
            self.zapiszDoPliku(nazwaPliku)
            oknoDialogowe.destroy()

        potwierdz = Button(oknoDialogowe, text="Potwierdz", command=potwiedzZapis)
        potwierdz.pack()

    def zapiszDoPliku(self, nazwaPliku):
        plik = open(nazwaPliku, "w")
        plik.write(str(self.czlowiek.getCzyZywy()) + '\n')
        for i in self.organizmy:
            if i.getCzyZywy():
                plik.write(i.nazwa + " ")
                plik.write(str(i.getX()) + " ")
                plik.write(str(i.getY()) + " ")
                plik.write(str(i.getInicjatywa()) + " ")
                plik.write(str(i.getWiek()) + " ")
                plik.write(str(i.getSila()) + " ")
                if isinstance(i, Czlowiek):
                    plik.write(str(i.getPodstawowaSila()) + " ")
                    plik.write(str(i.getBlokadaUmiejetnosci()) + " ")
                plik.write('\n')

    def wczytaj(self):
        oknoDialogowe = Tk()
        tekst = Entry(oknoDialogowe)
        tekst.pack()

        def potwierdzWczytanie():
            nazwaPliku = tekst.get()
            self.wczytajZPliku(nazwaPliku)
            oknoDialogowe.destroy()

        potwierdz = Button(oknoDialogowe, text="Potwierdz", command=potwierdzWczytanie)
        potwierdz.pack()

    def wczytajZPliku(self, nazwaPliku):
        plik = open(nazwaPliku, "r")
        statusCzl = plik.readline()
        self.tablicaOrganizmow = []
        for i in range(0, self._wysokosc):
            wiersz = []
            for j in range(0, self._szerokosc):
                wiersz.append(None)
            self.tablicaOrganizmow.append(wiersz)
        self.organizmy = []
        self.plansza.panelGry.delete("all")
        while True:
            organizm = plik.readline()
            if organizm == "":
                break
            daneOrganizmu = organizm.split(" ")
            x = int(daneOrganizmu[1])
            y = int(daneOrganizmu[2])
            polozenie = Polozenie(x, y)
            if daneOrganizmu[0] == "Czlowiek":
                czlowiek = Czlowiek(self, polozenie, (daneOrganizmu[3]), (daneOrganizmu[4]), (daneOrganizmu[5]),
                                    int(daneOrganizmu[6]), int(daneOrganizmu[7]))
                self.dodajOrganizm(czlowiek)
                self.czlowiek.setCzyZywy(statusCzl)
                self.czlowiek = czlowiek
            else:
                org = self.wczytajOrganizm(daneOrganizmu, self, x, y)
                self.dodajOrganizm(org)
            if not organizm:
                break
        plik.close()
        self.plansza.rysujSwiat()
        self.plansza.komentator.insert('end', "Wczytano z pliku" + '\n')

    def wczytajOrganizm(self, daneOrganizmu, swiat, x, y):
        polozenie = Polozenie(x, y)
        if daneOrganizmu[0] == "Barszcz_Sosnowskiego":
            return BarszczSosnowskiego(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Guarana":
            return Guarana(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Mlecz":
            return Mlecz(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Trawa":
            return Trawa(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Wilcze_Jagody":
            return WilczeJagody(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Antylopa":
            return Antylopa(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Cyberowca":
            return Cyberowca(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Lis":
            return Lis(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Owca":
            return Owca(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Wilk":
            return Wilk(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        elif daneOrganizmu[0] == "Zolw":
            return Zolw(swiat, polozenie, daneOrganizmu[3], daneOrganizmu[4], daneOrganizmu[5])
        else:
            return None

    def getLiczbaSasiednichPol(self):
        return self._liczbaSasiednichPol

    def getWysokosc(self):
        return self._wysokosc

    def getSzerokosc(self):
        return self._szerokosc

    def getStatusCzlowieka(self):
        return self._statusCzlowieka