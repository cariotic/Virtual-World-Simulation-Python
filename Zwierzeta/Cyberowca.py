from Zwierze import Zwierze
from Polozenie import Polozenie


class Cyberowca(Zwierze):
    kolor = "magenta"

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek,sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)
        self.nazwa = "Cyberowca"

    def rozmnazanie(self, polozenie: Polozenie):
        return Cyberowca(self._swiat, polozenie, 4, 0, 11)

    def znajdzBarszczSosonowskiego(self):
        for i in range(self._swiat.getWysokosc()):
            for j in range(self._swiat.getSzerokosc()):
                if self._swiat.tablicaOrganizmow[i][j] is not None and\
                        self._swiat.tablicaOrganizmow[i][j].getNazwa() == "Barszcz_Sosnowskiego":
                    return self._swiat.tablicaOrganizmow[i][j].polozenie
        return None

    def idzDoBarszczu(self, polozenieBarszczu: Polozenie):
        x = self.polozenie.x
        y = self.polozenie.y
        if polozenieBarszczu.y < self.polozenie.y:
            if self._swiat.tablicaOrganizmow[y - 1][x] is None:
                self.polozenie.y -= 1
                self._swiat.tablicaOrganizmow[y - 1][x] = self
                self._swiat.tablicaOrganizmow[y][x] = None
            else:
                self._swiat.tablicaOrganizmow[y - 1][x].kolizja(self)
        elif polozenieBarszczu.y > self.polozenie.y:
            if self._swiat.tablicaOrganizmow[y + 1][x] is None:
                self.polozenie.y += 1
                self._swiat.tablicaOrganizmow[y + 1][x] = self
                self._swiat.tablicaOrganizmow[y][x] = None
            else:
                self._swiat.tablicaOrganizmow[y + 1][x].kolizja(self)
        elif polozenieBarszczu.x > self.polozenie.x:
            if self._swiat.tablicaOrganizmow[y][x + 1] is None:
                self.polozenie.x += 1
                self._swiat.tablicaOrganizmow[y][x + 1] = self
                self._swiat.tablicaOrganizmow[y][x] = None
            else:
                self._swiat.tablicaOrganizmow[y][x + 1].kolizja(self)
        elif polozenieBarszczu.x < self.polozenie.x:
            if self._swiat.tablicaOrganizmow[y][x - 1] is None:
                self.polozenie.x -= 1
                self._swiat.tablicaOrganizmow[y][x - 1] = self
                self._swiat.tablicaOrganizmow[y][x] = None
            else:
                self._swiat.tablicaOrganizmow[y][x - 1].kolizja(self)

    def akcja(self):
        polozenieBarszczu = self.znajdzBarszczSosonowskiego()
        if polozenieBarszczu is not None:
            self.idzDoBarszczu(polozenieBarszczu)
        else:
            self.ruch()
