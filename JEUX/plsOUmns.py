import math
import random
print("  >==|Jeu + ou -|==<   \n")

print("     version 3.6")
print("\nValeur minimum ?\n")

vmin=int(input())
print("  >==|Jeu + ou -|==<   \n")

print("     version 3.6")
print("\nValeur maximum ?\n")

vmax=int(input())

if(vmin>vmax):
  print("[ERREUR]\nLa valeur minimum\nest plus grande\nque la maximum")
if(vmax>99999999):
  print("[ERREUR]\nLa valeur maximum\nest trop grande")

val = random.randint(vmin,vmax)
while(1):
  resul = int(input("Propsition ~ "))
  if(resul == val): 
    print("\n\n *** OUI ! Bravo ***\n")
    print("   [TAPEZ 'exit']\n")
    print("      ~",val,"~")
    break
  elif(resul < val):
    print("#####################\n=>Entre",vmin,"et",vmax,"\n\nC'est plus que",resul,"\n\n#########################")
  elif(resul==9999999999):
    print(val)
  else:
    print("#####################\n=>Entre",vmin,"et",vmax,"\n\nC'est moins que",resul,"\n\n#########################")