# on importe les librairies requises
import random
guess = -1
essaie = 0
jouer_encore = ""
jouer = True
# on definie la limite initiale
limites1 = "1"
limites2 = "100"

# on cree une fonction pour le choix de la borne
def les_limites():
    global limites2
    global limites1
    # on demande la borne
    limites1 = input("Quelle est la premiere limite de nombre que vous voulez : ")
    limites2 = input("Quelle est la deuxieme limite de nombre que vous voulez : ")

    # on iverse les variables si la premiere est plus grande que la deuxieme
    if int(limites2) < int(limites1):
        limites1, limites2 = limites2, limites1

    jeu_de_devinettes()



# on cree une variable pour le jeu de devinette
def jeu_de_devinettes():
    # on genere le nombre
    global the_number
    the_number = random.randint(int(limites1), int(limites2))
    # on cree le jeu avec les conditions requise pour activer le jeu
    return the_number


# on appelle les deux fonctions dans le bon ordre
def demande():
    demande = input("Voulez-vous choisir les bornes? O / N : ").lower()
    if demande == "o":
        les_limites()



while jouer:
    demande()
    jeu_de_devinettes()
    while guess != the_number:
        # on demande le guess
        guess = int(input("Entrez un nombre svp : "))
        # si il est plus petit on le fait retenter sa chance en ajoutant 1 essaies
        if guess > the_number:
            print("Plus petit")
            essaie += 1
        # si il est plus grand on le fait retenter sa chance en ajoutant 1 essaies
        elif guess < the_number:
            print("Plus grand")
            essaie += 1
        # si c'est le bon nombre, on lui dis son nombre d'essaies et on lui demande si il veut rejouer
        else:
            essaie += 1
            print("Game Over! Le nombre etait", the_number, ". Vous avez reussit en ", essaie, "essaies")
            jouer_encore = input("Voulez-vous rejouer? O ou N : ").lower()
            essaie = 0
        # si c'est non on quitte
    if jouer_encore == "n":
        print("Au revoir")
        jouer = False
