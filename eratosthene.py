"""Forme le crible d'eratosthène"""
class eratosthene :
    def __init__(self,n):
        self.taille = n
        self.tableau = [True] * n
        self.tableau[0] = False
        self.tableau[1] = False
        self.crible = []
    def creationTable(self) :
        for i in range (2,self.taille) :
            if self.tableau[i] :
                for j in range (i*i,self.taille,i) :
                    self.tableau[j] = False
        for i in range(len(self.tableau)) :
            if self.tableau[i] :
                self.crible.append(i)
        return self.crible