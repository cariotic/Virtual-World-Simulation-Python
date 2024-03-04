from Roslina import Roslina
from Polozenie import Polozenie
from Organizm import Organizm
import tkinter as tk


class BarszczSosnowskiego(Roslina):
    kolor = "lime"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Barszcz_Sosnowskiego"

    def rozmnazanie(self, polozenie: Polozenie):
        return BarszczSosnowskiego(self._swiat, polozenie, 0, 0, 10)

    def zabij(self, atakujacy: Organizm):
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
        atakujacy.setCzyZywy(False)

    def akcja(self):
        if self.probaRozmnozenia():
            self._swiat.plansza.komentator.insert(tk.END, "Nowa roslina: " + self.nazwa + '\n')
        x = self.polozenie.x
        y = self.polozenie.y
        if y > 0 and self._swiat.tablicaOrganizmow[y - 1][x] is not None and self._swiat.tablicaOrganizmow[y - 1][x].getNazwa() != self.nazwa\
                and self._swiat.tablicaOrganizmow[y - 1][x].nazwa != "Cyberowca":
            ofiara = self._swiat.tablicaOrganizmow[y - 1][x].getNazwa()
            self.zabij(self._swiat.tablicaOrganizmow[y - 1][x])
            self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + ofiara + '\n')
        if y < self._swiat.getWysokosc() - 1 and self._swiat.tablicaOrganizmow[y + 1][x] is not None and self._swiat.tablicaOrganizmow[y + 1][x].getNazwa() != self.nazwa\
                and self._swiat.tablicaOrganizmow[y + 1][x].nazwa != "Cyberowca":
            ofiara = self._swiat.tablicaOrganizmow[y + 1][x].getNazwa()
            self.zabij(self._swiat.tablicaOrganizmow[y + 1][x])
            self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + ofiara + '\n')
        if x < self._swiat.getSzerokosc() - 1 and self._swiat.tablicaOrganizmow[y][x + 1] is not None and self._swiat.tablicaOrganizmow[y][x + 1].getNazwa() != self.nazwa\
                and self._swiat.tablicaOrganizmow[y][x + 1].nazwa != "Cyberowca":
            ofiara = self._swiat.tablicaOrganizmow[y][x + 1].getNazwa()
            self.zabij(self._swiat.tablicaOrganizmow[y][x + 1])
            self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + ofiara + '\n')
        if x > 0 and self._swiat.tablicaOrganizmow[y][x - 1] is not None and self._swiat.tablicaOrganizmow[y][x - 1].getNazwa() != self.nazwa\
                and self._swiat.tablicaOrganizmow[y][x - 1].nazwa != "Cyberowca":
            ofiara = self._swiat.tablicaOrganizmow[y][x - 1].getNazwa()
            self.zabij(self._swiat.tablicaOrganizmow[y][x - 1])
            self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + ofiara + '\n')

    def kolizja(self, atakujacy: Organizm):
        if atakujacy.nazwa == "Cyberowca":
            self.zabij(self)
            self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
            self._swiat.tablicaOrganizmow[self.polozenie.y][self.polozenie.x] = atakujacy
            self._swiat.plansza.komentator.insert(tk.END, atakujacy.nazwa + " zabija " + self.nazwa + '\n')
        else:
            self.zabij(atakujacy)
            self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + atakujacy.nazwa + '\n')