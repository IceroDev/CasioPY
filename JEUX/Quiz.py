while(1):
  print("Annee de reference\npour l'IPC\n")
  print("1. 2013")
  print("2. 2000")
  print("3. 2010")
  rep = int(input("Votre reponse ~"))
  if(rep!=1):
    print("NO")
  elif(rep==1):
    print("Quel est la marque\ndu premier pc?\n")
    print("1. Samsung")
    print("2. Sony")
    print("3. Apple")
    rep = int(input("Votre reponse ~"))
    if(rep!=3):
      print("NO")
    elif(rep==3):
      print("Qui est Jeff Bezos ?\n\n")
      print("1. PDG de Amazon")
      print("2. PDG de Microsoft")
      print("3. PDG de Alibaba.fr")
      rep = int(input("Votre reponse ~"))
      if(rep!=1):
        print("NO")
      elif(rep==1):
        print("Quel site a cree Kim \nDotcom ?\n")
        print("1. HDS.TO")
        print("2. megaupload.fr")
        print("3. cpasbien.net")
        rep = int(input("Votre reponse ~"))
        if(rep!=2):
          print("NO")
        elif(rep==2):
          print("Combien coute +- le\nnouvel IPhone ?\n")
          print("1. 800$")
          print("2. 1100$")
          print("3. 1400$")
          rep = int(input("Votre reponse ~"))
          if(rep!=3):
            print("NO")
          elif(rep==3):
            print("Combien de 'r' dans\nle mot 'nouriture'?\n")
            print("1. 1 r")
            print("2. 2 r")
            print("3. 3 r")
            rep = int(input("Votre reponse ~"))
            if(rep!=3):
              print("NO")
            elif(rep==3):
              print("A quelle question \nsommes nous ?\n")
              print("1. 5eme")
              print("2. 7eme")
              print("3. 9eme")
              rep = int(input("Votre reponse ~"))
              if(rep!=2):
                print("NO")
              elif(rep==2):
                print("Un fichier .bat \nouvre :\n")
                print("1. Une commande au pc")
                print("2. Le film Batman")
                print("3. Une photo")
                rep = int(input("Votre reponse ~"))
                if(rep!=1):
                  print("NO")
                elif(rep==1):
                  print("Ce quiz est il\nsympa ?\n")
                  print("1. Non, il pue")
                  print("2. Oui, j'adore")
                  print("3. Tg, next question")
                  rep = int(input("Votre reponse ~"))
                  if(rep!=3):
                    print("NO")
                  elif(rep==3):
                    print("Roulette russe YEAH!\n\n")
                    
                    print("1. reponse 1")
                    print("2. reponse 2")
                    print("3. Go question 1 mdr")
                    import random
                    rdm = random.randint(1,2)
                    rep = int(input("Votre reponce ~"))
                    if(rep!=rdm):
                      print("NO")
                    else:
                      print("\n\n\n Bravo, tu as reussi\n\n(a perdre ton temps)\n")
                      break