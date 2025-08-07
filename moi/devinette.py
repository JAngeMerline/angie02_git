# jeu de devinnette
#Choisit un nombre au hasard entre 1 et 50
import random
nombre_secret= random.randint(1,50)
print("le nombre secret est: ", nombre_secret) # si je veux afficher le nombre secret
#demande a l'utilisateur de devinert un nombre entre 1 et 50

proposition=int(input("Entrer un nombre comprit entre 1 et 50: "))
#si la prposition n'est pas egal au nombre secret on continue
while proposition!= nombre_secret:
    if proposition< nombre_secret:
        print("trop petit")
    else:
        print("trop grand")
#demander a l'utilisateur d'entrer une nouvelle fois le mombre secret
    proposition=int(input("Essayer encore: "))

#l'utilisateur trouve le bon nombre

print("GENIAL!!!, vous avez trouver le bon nombre 🎉")