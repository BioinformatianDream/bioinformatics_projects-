sequence = "ATGCGTACGTTAG"

longueur = len(sequence)
A= sequence.count("A")
T= sequence.count("T")
C= sequence.count("C")
G= sequence.count("G")

print("Sequence ADN :",sequence)
print("longeur :",longueur)
print("A:",A)
print("T:",T)
print("C:",C)
print("G:",G)
# Calcul du pourcentage GC 

pourcentage_gc = ((G + C) / longueur) * 100

print("Pourcentage GC :", pourcentage_gc, "%")