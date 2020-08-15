import random
pers = ["Justine","Thomas","Alexandre","Marc","Lars","Jean","Abadja","Batman","Superman","Asterix","Daniel Radclife","Gandalf","Blanche Neige","Les Simpson","Indochine","Christophe Beaugrand","Les Schtoumphs","Steve Jobs","Lola","Vanina","Soprano"
,"Hitler","Nabila","Johnny Hallyday","Squeezie","Cyprien","Thibault Courtois","Tom Cruice","Vin Diesel","Phillippe Etchebest","Patrick Sebatien","AC-DC","Pascal le grand frere","Eden Hasard","Pythagore","Mickey Mouse","Didier Deschamps","Slimane"]
action = ["a the voice","En slip","Au MCDO","Chez Lola","A la patinoire","Chante Bella Ciao","Fait des mahs","Rale","Crie 'pololoo'","Rage sur Minecraft","Regarde C pas sorcier","Dans Koh-Lanta","Dans les anges","Imite Abadja","Galere en math"
,"Pleure son destin","Est/sont nazi","Va chez le gyneco","Disseque un veau","S'endort au cours","Va sur le 18-25","Avoue etre gay","Fait a manger","Vend du shit","Se fait embouiller","Vole la Joconde","Braque un MCDO","Vend ses cours de bio"]

pers2 = pers.copy()
action2 = action.copy()
P = random.randint(0,len(pers)-1)
A = random.randint(0,len(action)-1)
P2 = random.randint(0,len(pers2)-1)
A2 = random.randint(0,len(action2)-1)  
print("***Ta mere en slip***\n\n1 apres 60s\n0 si un joueur trouve")
print("Prenom(s) joueur(s) 1\n")
prenom1=input()
print("Prenom(s) joueur(s) 2\n")
prenom2=input()
print("\n\n\n",prenom2,"\n       TAPEZ 1\n")

while(1):   
  int1 = int(input())
  if(int1 != 1):
    print("ERREUR:\n\ncode:769\nCe code n'est pas\nreconnu veuillez \nrecommencer")
      
  else:
    print("########################")
    print("JOUEUR:",prenom1,"\n")
    print(pers[P])
    print(action[A])
    print("########################")
    int2 = int(input())
    if(int2!=1):
      print("ERREUR:\n\ncode:769\nCe code n'est pas\nreconnu veuillez \nrecommencer")
      
    if(int2==0):
      print("\n\n\n   *Equipe 1 Gagne*\n\n")
      break
    elif(int2==1):
      print("\n\n\n",prenom1,"\n       TAPEZ 1\n")
      int3 = int(input())
      if(int3!=1):
        print("ERREUR:\n\ncode:769\nCe code n'est pas\nreconnu veuillez \nrecommencer")
        
      else:
        print("########################")
        print("JOUEUR:",prenom2,"\n")
        print(pers2[P2])
        print(action2[A2])
        print("########################")
        int4 = int(input())
        if(int4==0):
          print("\n\n\n   *Equipe 2 Gagne*\n\n")
          break
        elif(int4 ==1):
          print("\n\n\n",prenom2,"\n       TAPEZ 1\n")
        else:
          print("ERREUR:\n\ncode:769\nCe code n'est pas\nreconnu veuillez \nrecommencer")