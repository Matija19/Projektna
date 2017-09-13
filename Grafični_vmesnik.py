import tkinter as tk
import model

class Štiri_v_vrsto:
    def __init__(self, okno):
        self.plosca = model.Plosca(10,10)

        self.obvestilo = tk.Label(okno, text = 'Na potezi je prvi igralec!',font =('Courier',20))
        self.obvestilo.grid(row = 0, column = 0,)

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.plosca.visina + 1):
            vrstica_gumbov = []
            for stolpec in range(self.plosca.sirina):
                def pritisni_gumb(stolpec = stolpec):
                    self.spusti(stolpec)
                if vrstica == 0:
                    gumb = tk.Button(prikaz_plosce, text = '', height = 4, width = 8, command = pritisni_gumb)
                    gumb.grid(row = vrstica, column = stolpec)
                    vrstica_gumbov.append(gumb)
                else:
                    gumb = tk.Button(prikaz_plosce, text = '', height = 4, width = 8, command = pritisni_gumb,state = 'disabled')
                    gumb.grid(row = vrstica, column = stolpec)
                    vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
            prikaz_plosce.grid(row = 1, column = 0, columnspan = 2)
        
        


    def spusti(self, stolpec):
        vrstica1 = self.plosca.spusti_krogec(stolpec) + 1
        vrednost = self.plosca.konec_igre()
        
        poteza = self.plosca.igralec_na_potezi()
        zmaga = self.plosca.zmagovalec()
        barva = self.plosca.oznaka()
        if vrstica1 <= 1:
            self.gumbi[0][stolpec].config(state = 'disabled')
            self.gumbi[vrstica1][stolpec].config(bg = self.plosca.oznaka())
        else:
            self.gumbi[vrstica1][stolpec].config(bg = self.plosca.oznaka())
        #PREVERIMO, ČE JE KONEC IGRE
        if vrednost == 0:
            self.obvestilo.config(text = 'Čestitke, zmagal je {}!'.format(zmaga),bg = 'green')
            for stolpec in range(self.plosca.visina):
                self.gumbi[0][stolpec].config(state = 'disabled')
        elif vrednost == 1:
            self.obvestilo.config(text = 'Rezultat je neodločen.')
        else:
            self.obvestilo.config(text = 'Na potezi je {}!'.format(poteza))
        
            
        
       

okno = tk.Tk()
plosca = Štiri_v_vrsto(okno)
okno.mainloop()
