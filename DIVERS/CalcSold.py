prix = float(input("\n\n\n\n\n\nPrix : "))
reduc = float(input("\n\n\n\n\n\nReduction en % : "))
print("     SOLDE CALC\n\n\n")
print("HORS REDUC :",prix)
p = prix-(reduc/100)*prix
print("AVEC REDUC :",p)
