from Polozenie import Polozenie
from Zwierze import Zwierze
import tkinter as tk


class Czlowiek(Zwierze):
    _kierunek = None
    _podstawowaSila = 5
    _blokadaUmiejetnosci = 0
    kolor = "cyan"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila, podstawowaSila, blokadaUmiejetnosci):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Czlowiek"
        self._podstawowaSila = podstawowaSila
        self._blokadaUmiejetnosci = blokadaUmiejetnosci

    def rozmnazanie(self, polozenie: Polozenie):
        return Czlowiek(self._swiat, polozenie, 4, 0, 5, 5, 0)

    def czyMoznaAktywowacUmiejetnosc(self):
        if self._blokadaUmiejetnosci == 0:
            return True
        else:
            self._swiat.plansza.komentator.insert(tk.END, "Nie mozna jeszcze aktywowac specjalnej umiejetnosci" + '\n')
            return False

    def aktywujUmiejetnosc(self):
        if self.getSila() == self._podstawowaSila and self._podstawowaSila <= 10:
            self._sila = 11
            self._blokadaUmiejetnosci = 11
            self._swiat.plansza.komentator.insert(tk.END, "Aktywowano specjalna umiejetnsc" + '\n')

    def ruch(self):
        x = self.polozenie.x
        y = self.polozenie.y
        if self._kierunek == 'g':
            if x > 0:
                if self._swiat.tablicaOrganizmow[y][x - 1] is None:
                    self.polozenie.x -= 1
                    self._swiat.tablicaOrganizmow[y][x - 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x - 1].kolizja(self)
        elif self._kierunek == 'd':
            if x < self._swiat.getWysokosc() - 1:
                if self._swiat.tablicaOrganizmow[y][x + 1] is None:
                    self.polozenie.x += 1
                    self._swiat.tablicaOrganizmow[y][x + 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x + 1].kolizja(self)
        elif self._kierunek == 'p':
            if y < self._swiat.getSzerokosc() - 1:
                if self._swiat.tablicaOrganizmow[y + 1][x] is None:
                    self.polozenie.y += 1
                    self._swiat.tablicaOrganizmow[y + 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y + 1][x].kolizja(self)
        elif self._kierunek == 'l':
            if y > 0:
                if self._swiat.tablicaOrganizmow[y - 1][x] is None:
                    self.polozenie.y -= 1
                    self._swiat.tablicaOrganizmow[y - 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y - 1][x].kolizja(self)
        elif self._kierunek == 'x':
            if self.czyMoznaAktywowacUmiejetnosc():
                self.aktywujUmiejetnosc()

    def akcja(self):
        if self._blokadaUmiejetnosci != 0:
            self._blokadaUmiejetnosci -= 1
            if self._sila != self._podstawowaSila:
                self._sila -= 1
        self.ruch()

    def getPodstawowaSila(self):
        return self._podstawowaSila

    def setPodstawowaSila(self, nowaSila):
        self._sila = nowaSila

    def getBlokadaUmiejetnosci(self):
        return self._blokadaUmiejetnosci

    def setKierunek(self, kierunek):
        self._kierunek = kierunek