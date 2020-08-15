import math
vs=3

s=float(input("|e| ecl et son ~"))
calc=s/vs
if(s<0):
  print("Le temps ne peut\npas etre negatif")
elif(calc<1):
  print("L'orage est tres \nproche (<1km)")
else:
  print("\n\nDistance entre vous\net l'orage\n")
  print("=>+-",round(calc),"km")
  