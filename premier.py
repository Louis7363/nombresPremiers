"""module permettant determiner si un nombre est premier"""
import math
import eratosthene
class nombre_premier :
    def __init__(self,n):
        self.n = n
        self.racine = math.sqrt(n)
        self.racine = math.floor(self.racine)
    def PremierNaive(self) :
        """Tente de diviser par tous les nommbres de 2 à N pour définir sa primarité"""
        if self.n == 1 :
            return False
        premier = True
        for i in range (2,self.n) :
            if self.n % i == 0:
                premier = False
        return premier

    def PremierRacine(self) :
        """Prends en paramètre le nombre,
        Ce doit être un entier
        Il va tester tout les nombres jusqu'a la racine carré du nombre pour vérifier si aucune des divisions n'a pour reste 0,
        Si ce n'est pas le cas alors le nombre est premier
        """
        if self.n == 1 :
            return False
        for i in range (2,self.racine+1) :
            if self.n % i == 0:
                return False
        return True
    def PremierRacineImpair(self) :
        """Idem que premier racine mais qu'avec les nombres impair (et 2)"""
        if self.n == 1 :
            return False
        if self.n != 2 :
            if self.n %2 != 0 :
                for i in range (3,self.racine+1,2) :
                    if self.n % i == 0:
                        return False
            else :
                return False
        return True
    def PremierCrible(self) :
        """Forme le crible d'eratosthène jusqu'à la racine carré du nombre et tente de diviser par toutes les nombres premiers."""
        if self.n == 1 :
            return False
        if self.n == 2 :
            return True
        table = eratosthene.eratosthene(self.racine)
        Crible = table.creationTable()

        for element in Crible :
            if self.n % element == 0 :
                return False
        return True