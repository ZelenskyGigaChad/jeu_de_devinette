#on importe les librairies requise
import random
#on definie la limite initiale
limites = "100"
#on cree une fonction pour le choix de la borne
def les_limites():
    global limites
#on demande la borne
    limites = input("Quelle est la limite de nombre que vous voulez : ")
#on retourne la variable
    return limites

#on cree une variable pour le jeu de devinette
def jeu_de_devinettes():
#on genere le nombre
    the_number = random.randint(1, int(limites))
    guess = 0
    essaie = 0
    jouer_encore = ""
    jouer = True
#on cree le jeu avec les conditions requise pour activer le jeu
    while jouer == True:
        while guess != the_number:
#on demande le guess
           guess = int(input("Entrez un nombre svp : "))
#si il est plus petit on le fait retenter sa chance en ajoutant 1 essaies
           if guess > the_number:
               print("Plus petit")
               essaie += 1
#si il est plus grand on le fait retenter sa chance en ajoutant 1 essaies
           elif guess < the_number:
               print("Plus grand")
               essaie += 1
#si c'est le bon nombre, on lui dis son nombre d'essaies et on lui demande si il veut rejouer
           else:
               print("Game Over! Le nombre etait", the_number, ". Vous avez reussit en ",essaie,"essaies")
               jouer_encore = input("Voulez-vous rejouer? O ou N : ").lower()
#si c'est non on quitte
           if jouer_encore == "n":
               jouer = False
#si c'est oui on rejoue
           elif jouer_encore == "o":
               jeu_de_devinettes()
#on appelle les deux fonctions dans le bon ordre
les_limites()
jeu_de_devinettes()
