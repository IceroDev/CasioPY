import random
rdm = ["Oui, c'est sur","Je dirais que non"]
while(1):
  print("Quel est ta question ?")
  print("EXE quand tu as fini")
  A = input()
  des = random.randint(0,len(rdm)-1)
  print("\n\n    ***Reponse***\n\n") 
  print(rdm[des])  