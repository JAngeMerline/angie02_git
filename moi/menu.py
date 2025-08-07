#Gestion d'une liste de courses

# 1.Créer une liste vide pour stocker les article que l'utilisateur va mettre
liste_courses = []

# 2. Boucle principale
while True: # cette boucle va tourner jusqu'a ce que l'utilisateur choiusisse de quitte.
    #on ajoute un menu ppur presenter les differentes option possible a l'utilisateur
    print("\nMenu :")
    print("1. Ajouter un article")
    print("2. Afficher la liste")
    print("3. Supprimer un article")
    print("4. Quitter")
#demander a l'utilisateur d'entrer son choix
    choix = input("Choisissez une option (1-4) : ")


    # Ajouter un article
    if choix == "1":
        article = input("Entrez le nom de l'article à ajouter : ")
        liste_courses.append(article)
        print(f"L'article '{article}' a été ajouté.") # message de confirmation

    # Afficher la liste
    elif choix == "2":
        if len(liste_courses) == 0: # verifier si la liste est vide
            print("Votre liste est vide.")
        else:
            print("Voici votre liste de courses :")
            for i, article in enumerate(liste_courses, 1):
                print(f"{i}. {article}")

    # pour supprimer la liste
    elif choix == "3":
        if len(liste_courses) == 0:
            print("Votre liste est vide. Rien à supprimer.")
        else:
            print("Voici votre liste :")
            for i, article in enumerate(liste_courses, 1):
                print(f"{i}. {article}")

            try:# on utilise try pour gerer les erreurs
                numero = int(input("Entrez le numéro de l'article à supprimer : "))
                if 1 <= numero <= len(liste_courses):
                    article_supprime = liste_courses.pop(numero - 1)
                    print(f"L'article '{article_supprime}' a été supprimé.")
                else:
                    print("Numéro invalide.")
            except ValueError: # c'est pour attrapper l'ereur pour ne pas [planter le programme.
                print("Veuillez entrer un numéro valide.")

    # Quitter le programme
    elif choix == "4":
        print("Merci d'avoir utilisé la liste de courses. À bientôt !")
        break

    else:
        print("Choix invalide, veuillez entrer un chiffre entre 1 et 4.")
