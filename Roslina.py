from Organizm import Organizm
from Polozenie import Polozenie
import random
import tkinter as tk

class Roslina(Organizm):

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)

    def zjedzenie(self):
        self._swiat.tablicaOrganizmow[self.polozenie.y][self.polozenie.x] = None
        self._czyZywy = False

    def czyAkcja(self):
        szansa = random.randint(0, 14)
        if szansa == 0:
            return True
        else:
            return False

    def probaRozmnozenia(self):
        if self.czyAkcja():
            y = self.polozenie.y
            x = self.polozenie.x
            kierunek = random.randint(0, 3)
            if kierunek == 0:  # gora
                if y > 0 and self._swiat.tablicaOrganizmow[y - 1][x] is None:
                    polozenieDziecka = Polozenie(x, y - 1)
                    dziecko = self.rozmnazanie(polozenieDziecka)
                    self._swiat.organizmy.append(dziecko)
                    self._swiat.tablicaOrganizmow[y - 1][x] = dziecko
                    return True
            elif kierunek == 1:  # dol
                if y < self._swiat.getWysokosc() - 1 and self._swiat.tablicaOrganizmow[y + 1][x] is None:
                    polozenieDziecka = Polozenie(x, y + 1)
                    dziecko = self.rozmnazanie(polozenieDziecka)
                    self._swiat.organizmy.append(dziecko)
                    self._swiat.tablicaOrganizmow[y + 1][x] = dziecko
                    return True
            elif kierunek == 2:  # prawo
                if x < self._swiat.getSzerokosc() - 1 and self._swiat.tablicaOrganizmow[y][x + 1] is None:
                    polozenieDziecka = Polozenie(x + 1, y)
                    dziecko = self.rozmnazanie(polozenieDziecka)
                    self._swiat.organizmy.append(dziecko)
                    self._swiat.tablicaOrganizmow[y][x + 1] = dziecko
                    return True
            elif kierunek == 3:  # lewo
                if x > 0 and self._swiat.tablicaOrganizmow[y][x - 1] is None:
                    polozenieDziecka = Polozenie(x - 1, y)
                    dziecko = self.rozmnazanie(polozenieDziecka)
                    self._swiat.organizmy.append(dziecko)
                    self._swiat.tablicaOrganizmow[y][x - 1] = dziecko
                    return True
            else:
                return False

    def akcja(self):
        if self.probaRozmnozenia():
            self._swiat.plansza.komentator.insert(tk.END, "Nowa roslina: " + self.nazwa + '\n')

    def kolizja(self, atakujacy: Organizm):
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
        atakujacy.polozenie = self.polozenie
        self.zjedzenie()
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = atakujacy
        self._swiat.plansza.komentator.insert(tk.END, atakujacy.nazwa + " zjada " + self.nazwa + '\n')
