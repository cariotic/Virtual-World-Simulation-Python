from Zwierze import Zwierze
from Polozenie import Polozenie
from Organizm import Organizm
import random


class Zolw(Zwierze):
    kolor = "darkgreen"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek,sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Zolw"

    def rozmnazanie(self, polozenie: Polozenie):
        return Zolw(self._swiat, polozenie, 1, 0, 2)

    def czyOdbilAtak(self, atakujacy: Organizm):
        if int(atakujacy.getSila()) < 5:
            return True
        else:
            return False

    def akcja(self):
        szansa = random.randint(0, 3)
        if szansa == 0:
            self.ruch()

    def kolizja(self, atakujacy: Organizm):
        if atakujacy.getNazwa() == self.nazwa and self.probaRozmnozenia():
            self._swiat.komentator.insert('end', "Nowe zwierze: " + self.nazwa + '\n')
        elif self.czyOdbilAtak(atakujacy):
            self._swiat.plansza.komentator.insert('end', self.nazwa + " odparl atak" + '\n')
        else:
            self.walka(atakujacy)

