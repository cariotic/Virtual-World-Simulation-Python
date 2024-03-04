from Zwierze import Zwierze
from Polozenie import Polozenie
import random
import tkinter as tk


class Lis(Zwierze):
    kolor = "orange"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek,sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Lis"

    def rozmnazanie(self, polozenie: Polozenie):
        return Lis(self._swiat, polozenie, 7, 0, 3)

    def ruch(self):
        kierunek = random.randint(0, 3)
        x = self.polozenie.x
        y = self.polozenie.y
        if kierunek == 0:
            if y > 0:
                if self._swiat.tablicaOrganizmow[y - 1][x] is None:
                    self.polozenie.y -= 1
                    self._swiat.tablicaOrganizmow[y - 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    if self._swiat.tablicaOrganizmow[y - 1][x].getSila() <= self._sila:
                        self._swiat.tablicaOrganizmow[y - 1][x].kolizja(self)
                    else:
                        self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " wyczul silniejszy organizm" + '\n')
        elif kierunek == 1:
            if y < self._swiat.getWysokosc() - 1:
                if self._swiat.tablicaOrganizmow[y + 1][x] is None:
                    self.polozenie.y += 1
                    self._swiat.tablicaOrganizmow[y + 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    if self._swiat.tablicaOrganizmow[y + 1][x].getSila() <= self._sila:
                        self._swiat.tablicaOrganizmow[y + 1][x].kolizja(self)
                    else:
                        self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " wyczul silniejszy organizm" + '\n')
        elif kierunek == 2:
            if x < self._swiat.getSzerokosc() - 1:
                if self._swiat.tablicaOrganizmow[y][x + 1] is None:
                    self.polozenie.x += 1
                    self._swiat.tablicaOrganizmow[y][x + 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    if self._swiat.tablicaOrganizmow[y][x + 1].getSila() <= self._sila:
                        self._swiat.tablicaOrganizmow[y][x + 1].kolizja(self)
                    else:
                        self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " wyczul silniejszy organizm" + '\n')
        elif kierunek == 3:
            if x > 0:
                if self._swiat.tablicaOrganizmow[y][x - 1] is None:
                    self.polozenie.x -= 1
                    self._swiat.tablicaOrganizmow[y][x - 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    if self._swiat.tablicaOrganizmow[y][x - 1].getSila() <= self._sila:
                        self._swiat.tablicaOrganizmow[y][x - 1].kolizja(self)
                    else:
                        self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " wyczul silniejszy organizm" + '\n')