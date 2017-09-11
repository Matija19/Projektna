import tkinter as tk

class Stevec:
    def __init__(self, okno):
        self.stevec = 0

        gumbi = tk.Frame(okno)
        self.gumb_desno = tk.Button(gumbi, text = 'Desno', command = self.desno)
        self.gumb_levo = tk.Button(gumbi, text = 'Levo', command = self.levo)
        gumb_spusti = tk.Button(gumbi, text = 'Spusti', command = self.spusti)
        self.prikaz_pozicije = tk.Label(okno, text = int('0')) # aj ta int kul??

        self.prikaz_pozicije.pack()
        self.gumb_desno.grid(row = 0, column = 2)
        gumb_spusti.grid(row = 0, column = 1)
        self.gumb_levo.grid(row = 0, column = 0)
        gumbi.pack()
        self.osvezi_prikaz()

    def osvezi_prikaz(self):
        self.prikaz_pozicije.configure(text = str (self.stevec))
#bom še vklopil
        if self.stevec <= 7:
            self.gumb_desno.config(state = 'normal')
        else:
            self.gumb_desno.config(state = 'disabled')
        if self.stevec < 1:
            self.gumb_levo.config(state = 'disabled')
        else:
            self.gumb_levo.config(state = 'normal')

    def desno(self):
        self.stevec += 1
        self.osvezi_prikaz()
    
    def spusti(self):
        self.stevec = 0
        self.osvezi_prikaz()

    def levo(self):
        self.stevec -= 1
        self.osvezi_prikaz()


okno = tk.Tk()
stevec = Stevec(okno)
okno.mainloop()
