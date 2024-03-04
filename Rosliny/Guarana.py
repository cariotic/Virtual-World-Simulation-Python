from Roslina import Roslina
from Polozenie import Polozenie
from Organizm import Organizm
import tkinter as tk


class Guarana(Roslina):
    kolor = "red"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Guarana"

    def rozmnazanie(self, polozenie: Polozenie):
        return Guarana(self._swiat, polozenie, 0, 0, 0)

    def kolizja(self, atakujacy: Organizm):
        atakujacy.setSila(int(atakujacy.getSila()) + 3)
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
        atakujacy.polozenie = self.polozenie
        self.zjedzenie()
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = atakujacy
        self._swiat.plansza.komentator.insert(tk.END, atakujacy.nazwa + " zjada " + self.nazwa
                                              + " czym zwieksza swoja sile o 3" + '\n')
