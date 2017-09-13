class Plosca:
    def __init__(self, visina = 8, sirina = 8):
        self.visina = visina
        self.sirina = sirina
        self.krogci_prvi_igralec = []
        self.krogci_drugi_igralec = []
 

#Plošča je v redu
    def __repr__(self):
        return 'Plosca(visina = {}, sirina = {})'.format(self.visina,self.sirina)
    
#SPUSTI KROGEC DELA ODLIČNO
    def spusti_krogec(self, sirina):
        stevilka_vrstice = self.visina - 1
        while (stevilka_vrstice, sirina) in self.krogci_prvi_igralec or (stevilka_vrstice, sirina) in self.krogci_drugi_igralec:
                stevilka_vrstice -= 1
                if stevilka_vrstice < 0:
                    return False
        if len(self.krogci_prvi_igralec) <= len(self.krogci_drugi_igralec):
            self.krogci_prvi_igralec.append((stevilka_vrstice, sirina))
        else:
            self.krogci_drugi_igralec.append((stevilka_vrstice, sirina))
        return stevilka_vrstice
        #NAJ ŠE PREVERI, ČE JE IGRE KONEC
            

    def __str__(self):
        polja = []
        for i in range(self.visina):
            polja.append(self.sirina * [' '])

        for krogec in self.krogci_prvi_igralec:
            vrstica, stolpec = krogec
            polja[vrstica][stolpec] = '0'
        for krogec in self.krogci_drugi_igralec:
            vrstica, stolpec = krogec
            polja[vrstica][stolpec] = 'X'
 
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob


    def oznaka(self):
        if len(self.krogci_prvi_igralec) <= len(self.krogci_drugi_igralec):
            return 'RoyalBlue1'
        else:
            return 'red2'



    def stiri_v_vrsto(self, element, seznam):
        vrstica, stolpec = element
        if element not in seznam:
            seznam.append(element)
        seznam_vrstic = []
        seznam_stolpcev = []
        seznam_diagonala_pozitivna = []
        seznam_diagonala_negativna = []
        if len(seznam) < 4:
                return False
        else:
                for i in range(-3,4):
                        #za vrstice
                        if (vrstica + i, stolpec) in seznam:
                                seznam_vrstic.append(i)
                                if len(seznam_vrstic) == 4:
                                    return True
                        if (vrstica + i, stolpec) not in seznam:
                                seznam_vrstic = []
                        #za stolpce
                        if (vrstica, stolpec + i) in seznam:
                                seznam_stolpcev.append(i)
                                if len(seznam_stolpcev) == 4:
                                    return True
                        if (vrstica, stolpec + i) not in seznam:
                                seznam_stolpcev = []
                        #za pozitivno diagonalo
                        if (vrstica + i, stolpec - i) in seznam:
                                seznam_diagonala_pozitivna.append(i)
                                if len(seznam_diagonala_pozitivna) == 4:
                                    return True
                        if (vrstica + i, stolpec - i) not in seznam:
                                seznam_diagonala_pozitivna = []
                        #za negativno diagonalo
                        if (vrstica + i, stolpec + i) in seznam:
                                seznam_diagonala_negativna.append(i)
                                if len(seznam_diagonala_negativna) == 4:
                                    return True
                        if (vrstica + i, stolpec + i) not in seznam:
                                seznam_diagonala_negativna = []
                        
                return False



    def igralec_na_potezi(self):
        if len(self.krogci_prvi_igralec) <= len(self.krogci_drugi_igralec):
            return 'prvi igralec'
        else:
            return 'drugi igralec'

    def zmagovalec(self):
        if len(self.krogci_prvi_igralec) <= len(self.krogci_drugi_igralec):
            return 'drugi igralec'
        else:
            return 'prvi igralec'

    def vrni(self):
        if len(self.krogci_prvi_igralec) > len(self.krogci_drugi_igralec):
            return self.krogci_prvi_igralec
        else:
            return self.krogci_drugi_igralec


                 
                                                                             
#TO JE V REDU
    def konec_igre(self):
        if len(self.krogci_prvi_igralec + self.krogci_drugi_igralec) == self.sirina * self.visina:
            return 1
        elif self.stiri_v_vrsto(self.vrni()[len(self.vrni()) - 1], self.vrni()) == True:
            return 0
        else:
            return -1



plosca = Plosca()

        




