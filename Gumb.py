import tkinter as tk

def desno():
    print('Desno')

def spusti():
    print(vnosno_polje.get())

def levo():
    print('Premikam se levo')

okno = tk.Tk()


vnosno_polje = tk.Entry(okno)
gumbi = tk.Frame(okno)
gumb_desno = tk.Button(gumbi, text = 'Desno', command = desno)
gumb_levo = tk.Button(gumbi, text = 'Levo', command = levo)
gumb_spusti = tk.Button(gumbi, text = 'Spusti', command = spusti)
prikaz_pozicije = tk.Label(okno, text = '0')

gumb_desno.grid(row = 0, column = 2)
gumb_spusti.grid(row = 0, column = 1)
gumb_levo.grid(row = 0, column = 0)
prikaz_stevca.pack()
gumbi.pack()
vnosno_polje.pack()

okno.mainloop()
