from Roslina import Roslina
from Polozenie import Polozenie
from Organizm import Organizm
import tkinter as tk


class WilczeJagody(Roslina):
    kolor = "purple"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Wilcze_Jagody"

    def rozmnazanie(self, polozenie: Polozenie):
        return WilczeJagody(self._swiat, polozenie, 0, 0, 99)

    def zabij(self, ofiara: Organizm):
        self._swiat.tablicaOrganizmow[ofiara.polozenie.y][ofiara.polozenie.x] = None
        ofiara.setCzyZywy(False)

    def kolizja(self, atakujacy: Organizm):
        self.zabij(atakujacy)
        self._swiat.plansza.komentator.insert(tk.END, self.nazwa + " zabija " + atakujacy.nazwa + '\n')

