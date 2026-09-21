from fractran import Fraction, Facteur, Fractran


#Test de somme
somme = [Fraction(3, 2)]
facteurs = Facteur([2, 3, 5])
print(Fractran(somme).run(facteurs.nombre([3, 4])))


#Calcul de la somme 
somme_ij = {}
for i in range(1, 11):
    for j in range (1, 11):
        somme_ij[i,j] = Fractran(somme).run(facteurs.nombre([i, j]))
print(somme_ij)


#suite de fractran
print(Fractran([Fraction(3, 10), Fraction(4, 3)]).suite(15, 4))
print(Fractran([Fraction(3, 10), Fraction(4, 3)]).suite(15, 2))


#Fibonacci
print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]

sortie_brute = Fractran(fibonacci).suite(3, 1000) 
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)