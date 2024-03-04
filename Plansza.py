
from tkinter import *
from Swiat import Swiat

class Plansza(Frame):
    plansza = None
    _rozmiarPola = 25
    swiat = None
    panelGry = None
    komentator = None

    def __init__(self):
        self.plansza = Tk()
        self.plansza.title("autor: Joanna Symczyk")
        self.plansza.geometry("500x700")
        self.komentator = Text(self.plansza, height=200, width=500)
        self.komentator.place(x=0, y=530)
        self.swiat = Swiat(self)
        self.panelGry = Canvas(self.plansza, width=500, height=500)
        self.przyciski(self.plansza)
        self.rysujSwiat()
        self.plansza.mainloop()

    def rysujSwiat(self):
        for i in range(self.swiat.getWysokosc()):
            for j in range(self.swiat.getSzerokosc()):
                if self.swiat.tablicaOrganizmow[i][j] is not None:
                    self.panelGry.create_rectangle(self._rozmiarPola * i, self._rozmiarPola * j,
                                                   self._rozmiarPola * i + self._rozmiarPola,
                                                   self._rozmiarPola * j + self._rozmiarPola,
                                                   fill=self.swiat.tablicaOrganizmow[i][j].getKolor())
                else:
                    self.panelGry.create_rectangle(self._rozmiarPola * i, self._rozmiarPola * j,
                                                   self._rozmiarPola * i + self._rozmiarPola,
                                                   self._rozmiarPola * j + self._rozmiarPola,
                                                   fill="white")
        self.panelGry.pack()

    def wGore(self, event):
        self.swiat.czlowiek.setKierunek('g')
        self.swiat.wykonajTure()

    def wPrawo(self, event):
        self.swiat.czlowiek.setKierunek('p')
        self.swiat.wykonajTure()

    def wLewo(self, event):
        self.swiat.czlowiek.setKierunek('l')
        self.swiat.wykonajTure()

    def wDol(self, event):
        self.swiat.czlowiek.setKierunek('d')
        self.swiat.wykonajTure()

    def umiejetnosc(self, event):
        self.swiat.czlowiek.setKierunek('x')
        self.swiat.wykonajTure()

    def przyciski(self, plansza):
        zapisz = Button(plansza, text="Zapisz", command=lambda: self.swiat.zapisz(), height=25, width=50)
        zapisz.place(bordermode=OUTSIDE, x=0, y=500, width=50, height=30)
        wczytaj = Button(plansza, text="Wczytaj", command=lambda: self.swiat.wczytaj(), height=25, width=50)
        wczytaj.place(bordermode=OUTSIDE, x=50, y=500, width=50, height=30)
        wyczysc = Button(plansza, text="Wyczysc komentarze", command=lambda: self.wyczyscKomentarze(), height=25, width=70)
        wyczysc.place(bordermode=OUTSIDE, x=100, y=500, width=130, height=30)
        self.plansza.bind('<Up>', self.wGore)
        self.plansza.bind('<Down>', self.wDol)
        self.plansza.bind('<Right>', self.wPrawo)
        self.plansza.bind('<Left>', self.wLewo)
        self.plansza.bind('<x>', self.umiejetnosc)

    def wyczyscKomentarze(self):
        self.komentator.delete("1.0", "end")