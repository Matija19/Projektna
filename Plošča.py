class Plosca:
    def __init__(self, visina = 8, sirina = 8, krogci = None):
        self.visina = visina
        self.sirina = sirina
        if krogci is None:
            self.krogci = []
        else:
            self.krogci = krogci

    def __repr__(self):
        return 'Plosca(visina = {}, sirina = {}, krogci = {})'.format(self.visina,self.sirina,self.krogci)
    

    def polozi_krogec(self, krogec, koordinata):
        self.krogci.append(krogec)
        self.koordinata = koordinata

    def __str__(self):
        polja = []
        for i in range(self.visina):
            polja.append(self.sirina * [' '])

        for x, y in Krogec(koordinata):
            polja[x][y] = 1


        
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob

class Krogec:
    def __init__(self, koordinata, plosca):
        #popravi, da bo sam spuščal dol, brez obeh koordinat podanih
        self.plosca = plosca
        self.koordinata = koordinata
        self.plosca.polozi_krogec(self, koordinata)

    def __repr__(self):
        return 'Krogec({0})'.format(self.koordinata)

#tudi to odstrani        
plosca = Plosca()
krog1 = Krogec((1,1),plosca)
