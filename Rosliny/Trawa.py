from Roslina import Roslina
from Polozenie import Polozenie


class Trawa(Roslina):
    kolor = "green"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Trawa"

    def rozmnazanie(self, polozenie: Polozenie):
        return Trawa(self._swiat, polozenie, 0, 0, 0)

