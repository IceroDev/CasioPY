import random
print("\n\n <3 Love Calc v2 <3\n")
print(" Resultats Aleatoires\n")
print(" EXE pour commencer")
S = input()
des = random.randint(1,101) 
print("#####################")
print("\n  >~Prenom pers 1~<\n\n")
print("#####################")
A = input()
  
  
print("#####################")
print("\n  >~Prenom pers 2~<\n\n")
print("#####################")  
B = input()
  
print(A,"et",B,"\nsont compatibles a \n~-~-~-~-~-*-~-~-~-~-~-~-~-~-\n")
print(des,"%")
    
  
if(des>50):
  print("WOW ca peut marcher")
if(des<50):
  print("Ca ne peut pas macher")
if(des==50):
  print("Mouais bof bof")