while(True):
    exercice = input("\r\n=======\r\nChoisissez l'exercice à faire : ")

    if exercice == "1":
        # 1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
        # “positif” ou “négatif”.
        print("\r\n=======\r\nExercice " + exercice)
        a = int(input("Entrez un entier : "))

        if a >= 0:
            print("Positif")
        else:
            print("Négatif")

    elif exercice == "2":
        # 2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
        # négatif, et affiche ce résultat.
        print("\r\n=======\r\nExercice " + exercice)

        b = int(input("Veuillez entrer un entier : "))

        if b > 0:
            print("Strictement positif")
        elif b == 0:
            print("Nul")
        elif b < 0:
            print("Strictement négatif")

    elif exercice == "3":
        # 3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
        # prédéfinie évidemment).
        print("\r\n=======\r\nExercice " + exercice)

        c = float(input("Veuillez entrer un entier : "))

        if(c < 0):
            c = c * -1
        print("La valeur absolue est " + str(c))

    elif exercice == "4":
        # 4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
        # à l’entier supérieur).
        print("\r\n=======\r\nExercice " + exercice)
        d = float(input("Veuillez entrer un réel : "))

        decimale = d%1

        if(decimale < 0.5):
            d = int(d)
            print("Valeur arrondie : " + str(d))
        else:
            d = int(d) + 1
            print("Valeur arrondie : " + str(d))

    elif exercice == "5":
        # 5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
        # compte des années bissextiles).
        print("\r\n=======\r\nExercice " + exercice)

        e = int(input("Veuillez entrer un numéro de mois : "))

        if e in [1, 3, 5, 7, 8, 10, 12]:
            print("31")
        elif e == 2:
            print("28")
        else:
            print("30")

    elif exercice == "6":
        # 6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
        # 4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
        # (2000 était une année bissextile).
        print("\r\n=======\r\nExercice " + exercice)

        f = int(input("Entrez une année : "))

        fBisextile = False

        if((f % 4 == 0 and f % 100 != 0) or f % 400 == 0):
            print("Année bisextile")
        else:
            print("Année non bisextile")

    elif exercice == "7":
        # 7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
        # et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.
        print("\r\n=======\r\nExercice " + exercice)

        jour = input("Veuillez entrer un jour : ")
        mois = input("Veuillez entrer un mois : ")

        if(3 <= int(mois) <= 6):
            if(int(mois) == 3 and int(jour) < 21):
                saison = "C'est l'hivers"
            elif(int(mois) == 6 and int(jour) > 20):
                saison = "C'est l'été"
            else:
                saison = "C'est le printemps"

        if(6 <= int(mois) <= 9):
            if(int(mois) == 6 and int(jour) < 21):
                saison = "C'est le printemps"
            elif(int(mois) == 9 and int(jour) > 20):
                saison = "C'est l'automne"
            else:
                saison = "C'est l'été"

        if(9 <= int(mois) <= 12):
            if(int(mois) == 9 and int(jour) < 21):
                saison = "C'est l'été"
            elif(int(mois) == 12 and int(jour) > 20):
                saison = "C'est l'hivers"
            else:
                saison = "C'est l'automne"

        if(int(mois) <= 12 and int(mois) <= 3):
            if(int(mois) == 12 and int(jour) < 21):
                saison = "C'est l'automne"
            elif(int(mois) == 3 and int(jour) > 20):
                saison = "C'est le printemps"
            else:
                saison = "C'est l'hivers"

        print(saison)