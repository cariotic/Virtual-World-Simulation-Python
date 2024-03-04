from Roslina import Roslina
from Polozenie import Polozenie
import tkinter as tk


class Mlecz(Roslina):
    liczbaProbMlecza = 3
    kolor = "gold"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Mlecz"

    def rozmnazanie(self, polozenie: Polozenie):
        return Mlecz(self._swiat, polozenie, 0, 0, 0)

    def akcja(self):
        i = self.liczbaProbMlecza
        while i > 0:
            if self.probaRozmnozenia():
                self._swiat.plansza.komentator.insert(tk.END, "Nowa roslina: " + self.nazwa + '\n')
            i -= 1

