krog1 = '0'
krog2 = 'X'
znacka = True



class Plosca:
    def __init__(self, visina = 8, sirina = 8):
        self.visina = visina
        self.sirina = sirina
        self.krogci_prvi_igralec = []
        self.krogci_drugi_igralec = []


    def __repr__(self):
        return 'Plosca(visina = {}, sirina = {}'.format(self.visina,self.sirina)
    

    def spusti_krogec(self, znacka, vrstica, stolpec):
        # koordinata = ...
        if znacka == True:
            self.krogci_prvi_igralec.append((vrstica, stolpec))
            znacka = not znacka
        else:
            self.krogci_drugi_igralec.append((vrstica,stolpec))
            znacka = not znacka


#    def zasedena_polja(self, plosca):
#        zasedena = set()
#        for krogec in self.krogci:
            


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


    def stiri_v_vrsto(self):
        vrstice = []
        stolpci = []
        naj = 0
        naj2 = 0
        if len(self.krogci_prvi_igralec) < 4:
            return False
        else:
            for krogec in range(len(self.krogci_prvi_igralec[3:])):
                vrstica1, stolpec1 = self.krogci_prvi_igralec[krogec]
                vrstice.append(vrstica1)
                stolpci.append(stolpec1)
                for i in range(len(self.krogci_prvi_igralec[:krogec]) -1):
                    vrstica2, stolpec2 = self.krogci_prvi_igralec[i]
                    vrstice.append(vrstica2)
                    stolpci.append(stolpec2)
                    for j in range(len(self.krogci_prvi_igralec[:i]) - 1):
                        vrstica3, stolpec3 = self.krogci_prvi_igralec[j]
                        vrstice.append(vrstica3)
                        stolpci.append(stolpec3)                                            
                        for k in range(len(self.krogci_prvi_igralec[:j]) - 1):
                            vrstica4, stolpec4 = self.krogci_prvi_igralec[k]
                            vrstice.append(vrstica4)
                            stolpci.append(stolpec4)                                          
            if vrstica1 == vrstica2 and vrstica2 == vrstica3 and vrstica3 == vrstica4:
                for i in stolpci:
                    for j in stolpci:
                        if max(i - j) <= 4:
                            return True
                        else:
                            return False
            if stolpec1 == stolpec2 and stolpec2 == stolpec3 and stolpec3 == stolpec4:
                for i in vrstice:
                    for j in vrstice:
                        if max(i - j) <= 4:
                            return True
                        else:
                            return False                                    
             
            else:
                for i in range(3):
                    for j in range(len(vrstice[i]) - 1):
                        if vrstica[i] != vrstica[j] and stolpec[i] != stolpec[j]:
                            naj = max(abs(vrstica[i] - vrstica[j]))
                            naj2 = max(abs(stolpec[i] - vrstica[j]))
                            if naj == 3 and naj2 == 3:
                                return True
                        return False
                 
                                                                      


                                                           
                
 
                
            
        
        

#    def konec_igre(self):
        #if vsa polja zasedena: return True
        #elif 4 v vrsto: return True
        #else: return False
        

#tudi to odstrani        
plosca = Plosca()
#ZASEDENA POLJA
#KROGEC1, 2
