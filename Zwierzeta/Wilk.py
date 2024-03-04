from Zwierze import Zwierze
from Polozenie import Polozenie


class Wilk(Zwierze):
    kolor = "black"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek,sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Wilk"

    def rozmnazanie(self, polozenie: Polozenie):
        return Wilk(self._swiat, polozenie, 5, 0, 9)
