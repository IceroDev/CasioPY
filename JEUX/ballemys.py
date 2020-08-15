import math
import random
print("   >==|Jeu balle|==<   \n")

print("Ou est la balle ?")
print("   [1] ~ [2] ~ [3]\n")
print("~Votre propsition :")
val = random.randint(1,3)
while(1):
  resul = float(input())
  if(resul == val): 
    print("*** OUI ! Bravo ***")
    print("[TAPEZ 'exit']")
    break
  if(resul != val): 
    print("Haha, mauvais")
    print("Essaye encore")
