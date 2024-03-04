import tkinter as tk
from Polozenie import Polozenie
from abc import ABC, abstractmethod


class Organizm(ABC):
    polozenie = None
    kolor = "white"
    nazwa = ""

    def __init__(self, swiat, polozenie: Polozenie, inicjatywa, wiek, sila):
        self._czyZywy = True
        self._swiat = swiat
        self.polozenie = polozenie
        self._inicjatywa = inicjatywa
        self._wiek = wiek
        self._sila = sila

    @abstractmethod
    def probaRozmnozenia(self):
        pass

    @abstractmethod
    def rozmnazanie(self, polozenie: Polozenie):
        pass

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, atakujacy):
        pass

    def getCzyZywy(self):
        return self._czyZywy

    def setCzyZywy(self, czyZywy):
        self._czyZywy = czyZywy

    def getInicjatywa(self):
        return self._inicjatywa

    def setInicjatywa(self, inicjatywa):
        self._inicjatywa = inicjatywa

    def getWiek(self):
        return self._wiek

    def setWiek(self, wiek):
        self._wiek = wiek

    def getSila(self):
        return self._sila

    def setSila(self, sila):
        self._sila = sila

    def getNazwa(self):
        return self.nazwa

    def getX(self):
        return self.polozenie.x

    def getY(self):
        return self.polozenie.y

    def getKolor(self):
        return self.kolor