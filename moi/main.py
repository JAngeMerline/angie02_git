# creation de classes

class library:
    def __init__(self, nom, auteur, annee, genre):
        self.nom=nom
        self.auteur=auteur
        self.annee=annee
        self.genre=genre
book1= library("La belle au bois dormant", "Agata Cristie", 1870,"roman")
book2=library("les dix hommes noirs", "Etzer Vilaire", 2000,"roman")
book3=library("L'alchimiste","Paolo Ccelho",1988,"roman")
book4=library("le petit Prince", "Antoine de Saint Exupery", 1900, "roman")
print(book1.nom)
print(book1.auteur)
print(book1.annee)
print(book1.genre)
