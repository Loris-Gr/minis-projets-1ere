#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GRANDCHAMPl
#
# Created:     22/11/2021
# Copyright:   (c) GRANDCHAMPl 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

liste_couleurs=["pique","coeur","carreau","trefle"]                               #liste des couleurs

liste_valeurs=["As","2","3","4","5","6","7","8","9","10","valet","dame","roi"]    #liste des valeurs

jeu_de_cartes=[]



def creer_jeu():                                  #création du jeu de cartes
    for valeurs in liste_valeurs :                         #parcours de la liste de valeurs
        for couleurs in liste_couleurs :                         # la liste de couleurs
            jeu_de_cartes.append([valeurs,couleurs])             # le .append permet d'ajouter les valeurs aux couleurs
    return jeu_de_cartes

def melange() :                                   #mélange du jeu de cartes
    import random
    random.shuffle(jeu_de_cartes)
    return jeu_de_cartes

def distribue_carte(jeu_de_cartes,n) :            #distribution des cartes aux joueurs
    joueurs=[]                                #initialisation d'une liste qui contiendra les listes de joueurs
    for joueur in range(n):      #on répète l'action autant de fois qu'il y a de joueurs
        joueurs.append([])        #cette boucle for permet de créer des listes dans notre liste (autant de fois qu'il y a de joueurs)
    pot=[]

    while len(jeu_de_cartes) >= n:           #la boucle se répètera jusqu'à ce qu'il y est moins de cartes restantes que de joueurs
        for joueur in range(n):     #on répète l'action autant de fois qu'il y a de joueurs
            carte = jeu_de_cartes[0]         #on initialise carte à la 1ère carte de la liste
            joueurs[joueur].append(carte)    #on l'ajoute dans notre liste
            jeu_de_cartes.pop(0)             #et on l'a supprime

        if jeu_de_cartes != []:         #s'il reste des cartes (si le jeux de cartes distribué est différent d'une liste vide)
            pot=jeu_de_cartes

    return joueurs,pot

n=int(input("Nombre de joueurs :"))          #initialisation nombre de joueurs

creer_jeu()
melange()
joueurs,pot = distribue_carte(jeu_de_cartes,n)     #on initialise la liste joueurs et le pot grâce à notre fonction distibue_carte

for joueur in range(n):                            #pour afficher les cartes par joueurs
    print("joueur", joueur, " : ", joueurs[joueur], "\n")
print("pot : ", pot)

"""print(jeu_de_cartes)"""







