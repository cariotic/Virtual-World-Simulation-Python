from Zwierze import Zwierze
from Polozenie import Polozenie
from Organizm import Organizm
import random
import tkinter as tk


class Antylopa(Zwierze):
    _zasiegAntylopy = 2
    kolor = "tan"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Antylopa"

    def rozmnazanie(self, polozenie: Polozenie):
        return Antylopa(self._swiat, polozenie, 4, 0, 4)

    def czyUcieknie(self):
        szansa = random.randint(0, 1)
        if szansa == 0:
            return True
        else:
            return False

    def ucieczka(self):
        x = self.polozenie.x
        y = self.polozenie.y
        if y > 0 and self._swiat.tablicaOrganizmow[y - 1][x] is None:
            self.polozenie.y -= 1
            self._swiat.tablicaOrganizmow[y - 1][x] = self
            self._swiat.tablicaOrganizmow[y][x] = None
            return True
        if y < self._swiat.getWysokosc() - 1 and self._swiat.tablicaOrganizmow[y + 1][x] is None:
            self.polozenie.y += 1
            self._swiat.tablicaOrganizmow[y + 1][x] = self
            self._swiat.tablicaOrganizmow[y][x] = None
            return True
        if x < self._swiat.getSzerokosc() - 1 and self._swiat.tablicaOrganizmow[y][x + 1] is None:
            self.polozenie.x += 1
            self._swiat.tablicaOrganizmow[y][x + 1] = self
            self._swiat.tablicaOrganizmow[y][x] = None
            return True
        if x > 0 and self._swiat.tablicaOrganizmow[y][x - 1] is None:
            self.polozenie.x -= 1
            self._swiat.tablicaOrganizmow[y][x - 1] = self
            self._swiat.tablicaOrganizmow[y][x] = None
            return True
        return False

    def ruch(self):
        kierunek = random.randint(0, 3)
        x = self.polozenie.x
        y = self.polozenie.y
        if kierunek == 0:
            if y - self._zasiegAntylopy >= 0:
                if self._swiat.tablicaOrganizmow[y - self._zasiegAntylopy][x] is None:
                    self.polozenie.y -= self._zasiegAntylopy
                    self._swiat.tablicaOrganizmow[y - self._zasiegAntylopy][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y - self._zasiegAntylopy][x].kolizja(self)
        elif kierunek == 1:
            if y < self._swiat.getWysokosc() - self._zasiegAntylopy:
                if self._swiat.tablicaOrganizmow[y + self._zasiegAntylopy][x] is None:
                    self.polozenie.y += self._zasiegAntylopy
                    self._swiat.tablicaOrganizmow[y + self._zasiegAntylopy][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y + self._zasiegAntylopy][x].kolizja(self)
        elif kierunek == 2:
            if x < self._swiat.getSzerokosc() - self._zasiegAntylopy:
                if self._swiat.tablicaOrganizmow[y][x + self._zasiegAntylopy] is None:
                    self.polozenie.x += self._zasiegAntylopy
                    self._swiat.tablicaOrganizmow[y][x + self._zasiegAntylopy] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x + self._zasiegAntylopy].kolizja(self)
        else:
            if x - self._zasiegAntylopy >= 0:
                if self._swiat.tablicaOrganizmow[y][x - self._zasiegAntylopy] is None:
                    self.polozenie.x -= self._zasiegAntylopy
                    self._swiat.tablicaOrganizmow[y][x - self._zasiegAntylopy] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x - self._zasiegAntylopy].kolizja(self)

    def kolizja(self, atakujacy: Organizm):
        if self.czyUcieknie():
            if self.ucieczka():
                self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " ucieka" + '\n')
        else:
            self.walka(atakujacy)
