mot = input("Entrez un mot ~")
lettres=list(mot)
print(lettres)
while(1):
  print("Quelle lettre ?")
  num = int(input())
  print(lettres[num-1])
  if(num==0):
    print("debut+1:fin+1:int")
    break