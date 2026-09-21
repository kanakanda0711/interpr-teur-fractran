class Fraction:


    def __init__(self, numérateur, dénominteur):
        self.numérateur = numérateur
        self.dénominteur = dénominteur


    def est_entier(self, n):
        if n%self.dénominteur == 0:
            return True 
        else: 
            return False


    def valeur(self, n):
        return self.numérateur*(n//self.dénominteur)


class Facteur:


    def __init__(self, facteurs):
        self.facteurs = facteurs


    def nombre(self, L):
        a = 1
        for i in range(len(L)):
            a = a*self.facteurs[i]**L[i] 
        return a


    def décomposition(self, n):
        facteurs = []
        for i in self.facteurs:
            a = 0
            while n % i == 0:
                n = n//i
                a+=1
            facteurs.append(a)
        return facteurs


class Fractran: 


    def __init__(self, fractions):
        self.programme = fractions


    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n) == True:
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n


    def suite(self, n, N):
        L = [n]
        i = 0
        
        while i < len(self.programme):
            if N > len(L):
                if self.programme[i].est_entier(n) == True:
                    n = self.programme[i].valeur(n)
                    i = 0
                    L.append(n)
                else:
                    i += 1
            else: break
        return L
