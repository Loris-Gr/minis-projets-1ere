#-------------------------------------------------------------------------------
# Name:        BATAILLE NAVALE
# Purpose:
#
# Author:      LORIS ET ELYANDRE
#
# Created:     31/03/2022
# Copyright:   (c) GRANDCHAMPl 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import font
import tkinter.messagebox
from functools import partial
import random
import time
import sys
import os

root = Tk()
root.wm_title("Bataille navale")
root.configure(background='gray19')
font1 = font.Font(family='Comic Sans MS', size=12, weight='bold')           #
font_big = font.Font(family='Comic Sans MS', size=16, weight='bold')        # POLICE D'ÉCRITURE
font_normal = font.Font(family='Comic Sans MS', size=10, weight='normal')   #

bateaux = {"porte-avions": 1, "croiseurs": 2, "Sous-marins": 3, "Torpilleurs": 4}
IA = False


def recommencer_programme():
    '''
    Cette méthode recommence le script de la partie
    '''
    python = sys.executable
    os.execl(python, python, *sys.argv)


def tab_joueur():
    """
    génération d'un tableau en 2 dimension représentant celui d'un joueur

    :return: liste en 2 dimension
    """
    tableau = []
    t = []
    # création de la bordure supérieure
    t += (10 + 2) * ['# ']
    tableau.append(t)

    # création d'une ligne dans le tableau
    rad = ['# ']
    for r in range(0, 10):
        rad.append("~ ")
    # insertion d'une nouvelle ligne dans le tableau
    rad.append('# ')
    for k in range(0, 10):
        tableau.append(list(rad))
    # insertion du bord inférieur
    tableau.append(t)
    return tableau


def placer_bateau(bateau, tableau):
    """
    placer un bateau sur le tableau

    :paramètre bateau: donné le nom des bateaux
    :paramètre tableau: tableau d'un joueur donné
    """
    # w = 0
    while True:
        verifcoords = []
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        o = random.randint(0, 1)
        if o == 0:
            ori = "v"  # verticale
        else:
            ori = "h"  # horizontale
        # Si le bateau veut être placé en dehors des bords du tableau
        if (ori == "v" and y + bateaux[bateau] > 10) or (ori == "h" and x + bateaux[bateau] > 10):
            pass
            # w = 0
        else:
            if ori == "v":
                # Placement verticale
                # Si il n'y a pas de navires proches de la position : le placer
                for i in range(-1, (bateaux[bateau] + 1)):
                    for j in range(-1, 2):
                        verifcoords.append(tableau[y + i][x + j])
                if ': ' not in verifcoords:
                    for i in range(bateaux[bateau]):
                        tableau[y + i][x] = ': '
                    break
            #                else:
            #                    w = 0
            elif ori == "h":
                # Placement horizontale
                # Si il n'y a pas de navires proches de la position : le placer
                for i in range(-1, (bateaux[bateau] + 1)):
                    for j in range(-1, 2):
                        verifcoords.append(tableau[y + j][x + i])
                if ': ' not in verifcoords:
                    for i in range(bateaux[bateau]):
                        tableau[y][x + i] = ': '
                    break


#                sinon:
#                    w = 0


def placer_tous_bateaux(tableau):
    """
    Placer tous les bateaux sur le tableau donné

    :param tableau: donné le tableau du joueur
    """
    for bateau in bateaux:
        for _ in range(0, (5 - bateaux[bateau])):
            placer_bateau(bateau, tableau)


def popupwindow(msg):
    """
    Pop up window si la partie est finie

    :param msg: nom du joueur
    """
    réponse = tkMessageBox.askquestion("Partie terminée", msg + " Voulez-vous jouer encore ?")
    if réponse == "oui":
        recommencer_programme()
    elif réponse == "non":
        quit()


def nr_joueurs(number):
    """
    Configurer le nombre de joueurs
    :param nombre: nombre de joueurs requis
    """
    global IA
    # activer les boutons du joueur2
    for bt_list in chaque_boutons[1]:
        for bt in bt_list:
            bt['state'] = 'normal'
    # si l'autre joueur requis est l'IA
    if number == 1:
        joueur2_ou_IA.set("IA")
        IA = True
    else:
        # activer les boutons du joueur 2
        for bt_list in chaque_boutons[0]:
            for bt in bt_list:
                bt['state'] = 'normal'
        joueur2_ou_IA.set("joueur 2")


info = StringVar()
joueur2_ou_IA = StringVar()
chaque_boutons = []


def side_labels():
    """
    créer les boutons et Labels for the field
    """
    # info = StringVar()
    Label(root, text="BATAILLE NAVALE", fg="white", bg="gray19", font=font_big).grid(row=0, column=10, columnspan=9)
    Label(root, textvariable=info, fg="white", bg="gray19", font=font1).grid(row=12, column=6, columnspan=18)

    for _ in range(10):
        Label(root, text="   ", bg="gray19").grid(row=_, column=0)
    Button(root, width=7, height=1, text="1 joueur", font=font1, fg="white", activebackground="gray19",
           bg="gray19", command=lambda: nr_joueurs(1)).grid(row=2, column=1)
    Button(root, width=7, height=1, text="2 joueurs", font=font1, fg="white", activebackground="gray19",
           bg="gray19", command=lambda: nr_joueurs(2)).grid(row=3, column=1)
    Label(root, text="Détruire tout les bateaux pour gagner :", font=font_normal, fg="white", bg="gray19").grid(row=5, column=1)
    Label(root, text="1 Bateau de 4 cases", font=font_normal, fg="white", bg="gray19").grid(row=6, column=1)
    Label(root, text="2 Bateaux de 3 cases", font=font_normal, fg="white", bg="gray19").grid(row=7, column=1)
    Label(root, text="3 Bateaux de 2 cases", font=font_normal, fg="white", bg="gray19").grid(row=8, column=1)
    Label(root, text="4 Bateaux de 1 cases  ", font=font_normal, fg="white", bg="gray19").grid(row=9, column=1)

    for _ in range(10):
        Label(root, text="   ", bg="gray19").grid(row=_, column=2)

    for _ in range(10):
        Label(root, width=20, text="   ", bg="gray19").grid(row=_, column=25)


def tirs_ia(y_coord, x_coord, tab_joueur_1, ia_score):
    """
    IA méthode de tir

    :paramétrer y_coord: coordonnée y à tirer
    :paramétrer x_coord: coordonnée x à tirer
    :paramétrer tab_joueur_1: tableau à tirer
    :paramétrer ia_score: score de l'IA
    """
    # Si l'ordi gagne
    if ia_score == 20:
        popupwindow("L'ordinateur a gagné.")
    # Si l'ordi touche un bateau il rejoue
    if tab_joueur_1[y_coord][x_coord] == ': ':
        ia_score += 1
        tab_joueur_1[y_coord][x_coord] = 'X '
        chaque_boutons[0][y_coord - 1][x_coord - 1].configure(text="X", fg="black", bg="red3")
        # dépend d'où le reste du bateau est localisé, lui tiré dessus
        if tab_joueur_1[y_coord - 1][x_coord] == ': ':
            tirs_ia(y_coord - 1, x_coord, tab_joueur_1, ia_score)
        elif tab_joueur_1[y_coord + 1][x_coord] == ': ':
            tirs_ia(y_coord + 1, x_coord, tab_joueur_1, ia_score)
        elif tab_joueur_1[y_coord][x_coord - 1] == ': ':
            tirs_ia(y_coord, x_coord - 1, tab_joueur_1, ia_score)
        elif tab_joueur_1[y_coord][x_coord + 1] == ': ':
            tirs_ia(y_coord, x_coord + 1, tab_joueur_1, ia_score)
        else:
            # tirer sur une position aléatoire si le bateau est détruit
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            tirs_ia(y, x, tab_joueur_1, ia_score)
    elif tab_joueur_1[y_coord][x_coord] == 'X ' or tab_joueur_1[y_coord][x_coord] == 'O ':
        # si la position a déjà été touché, essayer une autre position
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        tirs_ia(y, x, tab_joueur_1, ia_score)
    else:
        # si l'eau a été touché, juste changer le bouton
        tab_joueur_1[y_coord][x_coord] = 'O '
        chaque_boutons[0][y_coord - 1][x_coord - 1].configure(text="O", fg="white")


def touche_ou_loupe(a, b, tableau, tout_boutons, info, joueur, tir_réussi_joueur1, tir_réussi_joueur2, ia_score, tableau2):
    """
    vérifié si le tir a été réussi ou manqué par le joueur

    :param a: clické position y
    :param b: clické position x
    :param tableau: tableau du joueur opposant
    :param tout_boutons: tout les boutons du tableau opposants
    :param info: écrire quelques infos sur l'écran
    :param joueur: nom joueur
    :param tir_réussi_joueur1: number of tir_réussi_joueur1
    :param tir_réussi_joueur2: number of tir_réussi_joueur2
    :param ia_score: number of IA tirs_touchés
    :param tableau2: own joueurs tableau
    """
    global IA
    # si l'on essaye de tirer sur une case touchée :

    if tableau[a + 1][b + 1] == 'O ' or tableau[a + 1][b + 1] == 'X ':
        fenetre = Tk()
        label4 = Label(fenetre, text="Tu as déjà tiré ici " + joueur + " !")
        label4.pack()
    elif tableau[a + 1][b + 1] == ': ':
        # si un bateau a été touché, changer la case du tableau
        fenetre = Tk()
        label4 = Label(fenetre, text="Touché ! Bien joué " + joueur + " !")
        label4.pack()
        tableau[a + 1][b + 1] = 'X '
        tout_boutons[a][b].configure(text="X", fg="black", bg="red3", activebackground="red3")
        # augmenter compteur de 1 et recommencer
        if joueur == "joueur 1":
            tir_réussi_joueur1 += 1
        else:
            tir_réussi_joueur2 += 1
    else:
        # Si l'on loupe, changer la case et faire attaquer l'IA
        fenetre = Tk()
        label4 = Label(fenetre, text="Il semble que tu es raté, " + joueur + "!")
        label4.pack()
        tableau[a + 1][b + 1] = 'O '
        tout_boutons[a][b].configure(text="O", fg="White", activeforeground="white")
        # afficher(IA)
        if IA:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            tirs_ia(y, x, tableau2, ia_score)
    if tir_réussi_joueur1 == 20 or tir_réussi_joueur2 == 20:
        # si un des joueurs à 20 touches, il gagne
        popupwindow(joueur + " a gagné !")


def side(joueur, toutboutons):
    """
    ordonner les boutons de chaque joueurs dans une grille

    :param joueur: noms joueurs
    :param toutboutons: tout les boutons de ce joueur
    """
    print(joueur)
    col = 4 if joueur == "joueur 1" else 15
    for row in range(10):
        for column in range(10):
            toutboutons[row][column].grid(row=1 + row, column=col + column)
    if joueur == "joueur 1":
        label2 = Label(root, text="Joueur 1", font=font1, fg="white", bg="gray19")
        label2.grid(row=11, column=4, columnspan=10)
    else:
        label3 = Label(root, textvariable=joueur2_ou_IA, font=font1, fg="white", bg="gray19")
        label3.grid(row=11, column=15, columnspan=10)


def tableau_boutons(tableau, info, joueur, tir_réussi_joueur1, tir_réussi_joueur2, ia_score, tableau2):
    """
    créer tout les boutons pour un joueur

    :param tableau: joueurs tableau
    :param info: écrire les infos de l'écran
    :param joueur: nom des joueurs
    :param joueur_1_tirs: nombre de tirs réussis du joueur 1
    :param tir_réussi_joueur2: nombre de tirs réussis du joueur 2
    :param ia_score: IA score
    :param tableau2: tableau opposant
    """
    toutboutons = []
    a = 0
    print(IA)
    for i in range(10):
        b = 0
        boutons = []
        for j in range(10):
            button = Button(root, width=2, height=1, font=font1, bg="sky blue", activebackground="sky blue",
                            command=partial(touche_ou_loupe, a, b, tableau, toutboutons,
                                            info, joueur, tir_réussi_joueur1, tir_réussi_joueur2, ia_score, tableau2), state="disable")
            boutons.append(button)
            b += 1
        # créer un tableau en 2 dimensions avec des boutons représentant le champ de bataille
        toutboutons.append(list(boutons))
        a += 1
    # stocker chaque boutons dans une liste pour plus tard dans l'accès global
    chaque_boutons.append(toutboutons)
    side(joueur, toutboutons)


def espace_tableau_milieu():
    """
    Insérer l'espace du milieu
    """
    for _ in range(10):
        Label(root, text="   ", bg="gray19").grid(row=1 + _, column=14)


def principal():
    """
    première méthode de jeu
    """
    tir_réussi_joueur1 = 0
    tir_réussi_joueur2 = 0
    ia_tirs_touchés = 0

    # initialiser le tableau du joueur
    tab_joueur_1 = tab_joueur()
    tab_joueur_2 = tab_joueur()

    # placer tous les bateaux sur le tableau
    placer_tous_bateaux(tab_joueur_1)
    placer_tous_bateaux(tab_joueur_2)

    # instert side labels
    info = StringVar()
    side_labels()

    # créer tout les boutons
    tableau_boutons(tab_joueur_1, info, "joueur 1", tir_réussi_joueur1, tir_réussi_joueur2, ia_tirs_touchés, tab_joueur_2)
    espace_tableau_milieu()
    tableau_boutons(tab_joueur_2, info, "joueur 2", tir_réussi_joueur1, tir_réussi_joueur2, ia_tirs_touchés, tab_joueur_1)


principal()
root.mainloop()
