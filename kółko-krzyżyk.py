import tkinter as tk
from tkinter import messagebox
import random

class KolkoIKrzyrzyk:
    def __init__(self, glowne_okno):
        self.glowne_okno = glowne_okno
        self.glowne_okno.title("Kółko i Krzyrzyk")
        self.aktualny_gracz = "X"
        self.plansza = [["" for _ in range(3)] for _ in range(3)]
        self.przyciski = [[None for _ in range(3)] for _ in range(3)]
        self.tryb_jednoosobowy = False
        self.utworz_menu()
        self.utworz_plansze()

def utworz_menu(self):
    ramka_trybu = tk.Frame(self.glowne_okno)
    ramka_trybu.grid(row=0, column=0, columnspan=3, pady= 10)

    tk.Label(ramka_trybu, text="Wybierz tryb: ", font=("Arial", 12)).pack(side=tk.LEFT)

    self.zmienna_trybu = tk.StringVar(value="dwoch")
    tk.RADIOBUTTON(ramka_trybu, text="Dwóch graczy", variable=self.zmienna_trybu, value="dwoch").pack(side=tk.LEFT)
    tk.RADIOBUTTON(ramka_trybu, text="Jeden gracz", variable=self.zmienna_trybu, value="jeden").pack(side=tk.LEFT)

    przycisk_rozpocznij = tk.button(ramka_trybu, text="Rozpocznij", command=self.rozpocznij_gre)
    przycisk_rozpocznij.pack(side=tk.LEFT, padx=10)