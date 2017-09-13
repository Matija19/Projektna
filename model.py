krog1 = '0'
krog2 = 'X'
znacka = True



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
#dodam še krogce z oznakami, da se ve, od katerega igralca so
        for krogec in self.krogci_prvi_igralec:
            vrstica, stolpec = krogec
            polja[vrstica][stolpec] = '0'
        for krogec in self.krogci_drugi_igralec:
            vrstica, stolpec = krogec
            polja[vrstica][stolpec] = 'X'
        #rob: da se boljše vidi igralna površina 
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob
#TO DELA V REDU
    def oznaka(self):
        if len(self.krogci_prvi_igralec) <= len(self.krogci_drugi_igralec):
            return 'X'
        else:
            return '0'
#v grafičnem vmesniku bom po vsakem pritisku na gumb klical funkcijo znacka, da zamenjam igralca

#ŠTIRI V VRSTO DELA PRAVILNO
    def stiri_v_vrsto(self, seznam):
        naj = 0
        naj2 = 0
        a = 0
        b = 0
        posebna_razlika = 0
        vrstice = []
        stolpci = []
        razlika = 0   
        dolzina = len(seznam)
        if len(seznam) < 4:
            return False
        else:
            for krogec in range(dolzina):
                vrstica1, stolpec1 = seznam[krogec]
                vrstice.append(str(vrstica1))
                stolpci.append(str(stolpec1))
                for i in range(dolzina):
                    if i == krogec:
                        continue
                    else:
                        vrstica2, stolpec2 = seznam[i]
                        vrstice.append(str(vrstica2))
                        stolpci.append(str(stolpec2))
                    for j in range(dolzina):
                        if j == krogec or j == i:
                            continue
                        else:
                            vrstica3, stolpec3 = seznam[j]
                            vrstice.append(str(vrstica3))
                            stolpci.append(str(stolpec3))
                        for k in range(dolzina):
                            if k == krogec or k == j or k == i:
                                continue
                            else:
                                vrstica4, stolpec4 = seznam[k]
                                vrstice.append(str(vrstica4))
                                stolpci.append(str(stolpec4))
                                if vrstica1 == vrstica2 and vrstica2 == vrstica3 and vrstica3 == vrstica4:
                                    for p in stolpci:
                                        for m in stolpci:
                                            razlika = max(razlika, abs(int(p) - int(m)))
                                    if razlika == 3:
                                        return True
                                elif stolpec1 == stolpec2 and stolpec2 == stolpec3 and stolpec3 == stolpec4:
                                    for p in vrstice:
                                        for m in vrstice:
                                            razlika = max(razlika, abs(int(p) - int(m)))
                                    if razlika == 3:
                                        return True                                             
                                else:
                                    for p in range(4):
                                        for m in range(4):
                                            if  p == m:
                                                continue
                                            else:
                                                naj = max(razlika, abs(int(vrstice[p]) - int(vrstice[m])))
                                                naj2 = max(razlika, abs(int(stolpci[p]) - int(stolpci[m])))
                                                a = int(stolpci[p]) - int(stolpci[m])
                                                b = int(vrstice[p]) - int(vrstice[m])
                                                posebna_razlika = max(posebna_razlika, abs(a-b))
                                                if naj == 3 and naj2 == 3 and posebna_razlika == 0:
                                                        return True                                     

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

                 
                                                                             
#TO JE V REDU
    def konec_igre(self):
        if len(self.krogci_prvi_igralec + self.krogci_drugi_igralec) == self.sirina * self.visina:
            return 1
        elif self.stiri_v_vrsto(self.krogci_prvi_igralec) == True:
            return 0
        else:
            return -1
        

#tudi to odstrani
plosca = Plosca()
#ZASEDENA POLJA
#KROGEC1, 2
