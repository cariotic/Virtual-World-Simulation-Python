from Organizm import Organizm
from Organizm import Polozenie
import random

class Zwierze(Organizm):

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        super().__init__(swiat, polozenie, inicjatywa, wiek, sila)

    def ruch(self):
        kierunek = random.randint(0, 3)
        x = self.polozenie.x
        y = self.polozenie.y
        if kierunek == 0:  # gora
            if y > 0:
                if self._swiat.tablicaOrganizmow[y - 1][x] is None:
                    self.polozenie.y -= 1
                    self._swiat.tablicaOrganizmow[y - 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y - 1][x].kolizja(self)
        elif kierunek == 1:  # dol
            if y < self._swiat.getWysokosc() - 1:
                if self._swiat.tablicaOrganizmow[y + 1][x] is None:
                    self.polozenie.y += 1
                    self._swiat.tablicaOrganizmow[y + 1][x] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y + 1][x].kolizja(self)
        elif kierunek == 2:  # prawo
            if x < self._swiat.getSzerokosc() - 1:
                if self._swiat.tablicaOrganizmow[y][x + 1] is None:
                    self.polozenie.x += 1
                    self._swiat.tablicaOrganizmow[y][x + 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x + 1].kolizja(self)
        elif kierunek == 3:  # lewo
            if x > 0:
                if self._swiat.tablicaOrganizmow[y][x - 1] is None:
                    self.polozenie.x -= 1
                    self._swiat.tablicaOrganizmow[y][x - 1] = self
                    self._swiat.tablicaOrganizmow[y][x] = None
                else:
                    self._swiat.tablicaOrganizmow[y][x - 1].kolizja(self)

    def zabij(self, atakujacy: Organizm):
        self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
        atakujacy.setCzyZywy(False)

    def probaRozmnozenia(self):
        y = self.polozenie.y
        x = self.polozenie.x
        kierunek = random.randint(0, 3)
        if kierunek == 0:  # gora
            if y > 0 and self._swiat.tablicaOrganizmow[y - 1][x] is None:
                polozenieDziecka = Polozenie(x, y - 1)
                dziecko = self.rozmnazanie(polozenieDziecka)
                self._swiat.organizmy.append(dziecko)
                return True
        elif kierunek == 1:  # dol
            if y < self._swiat.getWysokosc() - 1 and self._swiat.tablicaOrganizmow[y + 1][x] is None:
                polozenieDziecka = Polozenie(x, y + 1)
                dziecko = self.rozmnazanie(polozenieDziecka)
                self._swiat.organizmy.append(dziecko)
                return True
        elif kierunek == 2:  # prawo
            if x < self._swiat.getSzerokosc() - 1 and self._swiat.tablicaOrganizmow[y][x + 1] is None:
                polozenieDziecka = Polozenie(x + 1, y)
                dziecko = self.rozmnazanie(polozenieDziecka)
                self._swiat.organizmy.append(dziecko)
                return True
        elif kierunek == 3:  # lewo
            if x > 0 and self._swiat.tablicaOrganizmow[y][x - 1] is None:
                polozenieDziecka = Polozenie(x - 1, y)
                dziecko = self.rozmnazanie(polozenieDziecka)
                self._swiat.organizmy.append(dziecko)
                return True
        else:
            return False

    def czyOdbilAtak(self, atakujacy: Organizm):
        if self._sila > int(atakujacy.getSila()):
            return True
        else:
            return False

    def walka(self, atakujacy: Organizm):
        if self.czyOdbilAtak(atakujacy) is True:
            self.zabij(atakujacy)
            self._swiat.plansza.komentator.insert('end', self.nazwa + " zabija " + atakujacy.nazwa + '\n')
        else:
            self._swiat.tablicaOrganizmow[atakujacy.polozenie.y][atakujacy.polozenie.x] = None
            atakujacy.polozenie = self.polozenie
            self.zabij(self)
            self._swiat.tablicaOrganizmow[self.polozenie.y][self.polozenie.x] = atakujacy
            self._swiat.plansza.komentator.insert('end', atakujacy.nazwa + " zabija " + self.nazwa + '\n')

    def akcja(self):
        self.ruch()

    def kolizja(self, atakujacy: Organizm):
        if self.nazwa == atakujacy.getNazwa() and self.probaRozmnozenia():
            self._swiat.plansza.komentator.insert('end', "Nowe zwierze: " + self.nazwa + '\n')
        else:
            self.walka(atakujacy)
