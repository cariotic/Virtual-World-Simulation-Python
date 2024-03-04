from Zwierze import Zwierze
from Polozenie import Polozenie


class Owca(Zwierze):
    kolor = "grey"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Owca"

    def rozmnazanie(self, polozenie: Polozenie):
        return Owca(self._swiat, polozenie, 4, 0, 4)
