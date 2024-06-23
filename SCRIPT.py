import numpy as np
import matplotlib.pyplot as plt
import copy
from math import *
from random import randint
from copy import deepcopy

pt=[]
maxi=200000
mini=-maxi
nombre_point=8
# Coordonnees varient entre mini et maxi, generees aleaatoirement.
for k in range(nombre_point):
    pt.append((randint(mini,maxi),randint(mini,maxi)))
print(pt)

pt=((-9, 4), (10, 6), (-9, -2), (1, -8), (-2, 9))
n=len(pt)
d_terme=n-2
dt_range=n-1

def Dernier_Terme(chiffres_restant):
    """
    chiffres_restant: Tableau a deux dimensions
    Determine le dernier terme d'un tableau qui n'est pas une liste vide.
    (A l'envers pour optimiser car la plupart du temps ce terme sera a la fin.)
    """
    p_max_test=0
    len_range=len(chiffres_restant)
    for compteur_test in range(0,len_range):
        if chiffres_restant[len_range-1-compteur_test]!=[]:
            p_max_test=len_range-1-compteur_test
            return p_max_test

def Combinaison(choix_actuel,chiffres_restant,n):
    """
    n entier naturel (int) qui correspond au nombre de points
    choix_actuel: Liste de taille n-1
    chiffres_restant: Tableau a deux dimensions

    Fonction principale, utilise la recursivite.
    Permet de determiner toutes les combinaisons possibles de chemin afin de resoudre le probleme.
    S'arrete lorsqu'on a atteint la derniere combinaison
    """


    global pos_max
    """Cette variable est utilisee dans les differentes repetition de la fonction
    et on souhaite pouvoir la recuperer et avoir la meme quelque soit l'instant de la fonction"""
    dt_range=len(chiffres_restant)
    # Si on a pas encore atteint le dernier terme
    if chiffres_restant!=[[] for k in range(dt_range)]:
        # Recupere la position de la derniere liste non vide
        pos_max=Dernier_Terme(chiffres_restant)
        # Rafraichissement des donnees
        chiffres_restant[pos_max].remove(choix_actuel[pos_max+1])

        # Recursion
        if chiffres_restant[pos_max]==[]:
            choix_actuel,chiffres_restant=Combinaison(choix_actuel,chiffres_restant,n)

        # Si on en est pas au dernier terme
        if chiffres_restant!=[[] for k in range(dt_range)]:
            # Reinitialisaition des valeurs possibles pour les chiffres suivants
            for k in range(pos_max+1,dt_range):
                chiffres_restant[k]=[o for o in range(2,n+1)]
                for j in range(1,k+1):
                    chiffres_restant[k].remove(choix_actuel[j])

                choix_actuel[k+1]=chiffres_restant[k][0]


            choix_actuel[pos_max+1]=chiffres_restant[pos_max][0]

            return choix_actuel,chiffres_restant


    """ If et pas else car on doit pouvoir sortir de la fonction
    en renvoyant les valeurs adequate et donc cette condition doit etre testee apres etre sorti d'une possible plongee recursive"""
    if chiffres_restant==[[] for k in range(dt_range)]:
        # Valeur speciale de choix_actuel permettant de terminer le programme
        return choix_actuel,chiffres_restant

def Distance(combinaison,tableau_pos,n):
    distance_totale=0
    for x in range(n):
        distance_totale+=tableau_pos[combinaison[x]-1][combinaison[x+1]-1]

    return distance_totale

distances_tab=[[0 for j in range(n)] for i in range(n)]

# Creation de la matrice comportant les distances
for i in range(n):
    for j in range(n):
         #if i !=j:
         # j lignes et i colonnes
        distances_tab[i][j]=int(sqrt(((pt[i][0]-pt[j][0])**2)+(pt[i][1]-pt[j][1])**2))

#Affiche la matrice
print("Tableau des distances entre chaques points:")
for i in range(n):
    print([distances_tab[i][j] for j in range(n)])


# Ensemble des cominaisons a renvoyer
combi=[]

# servira pour creer les combinaisons
chiffres_restant=[[j for j in range(2,n+1)] for x in range(dt_range)]
choix_actuel=[0 for i in range(n+1)]

# Construction de la premiere Combinaison choisie
for j in range(0,dt_range):
    choix_actuel[j+1]=chiffres_restant[j][0]

    # Enleve les chiffres deja utilises pour les combinaisons suivantes et empeche de depasser le dernier terme du range
    for m in range(min(j+1,dt_range),dt_range):
        chiffres_restant[m].remove(choix_actuel[j+1])

choix_actuel[0],choix_actuel[n]=1,1

# Initialise les valeurs
choix_enregistre=copy.deepcopy(choix_actuel)
dist_enregistre=Distance(choix_enregistre,distances_tab,n)
print("dist de depart",dist_enregistre)
compteur=0
# Valeur que prendra choix_actuel a la fin (vois fonction Combinaison)
while chiffres_restant!=[[] for k in range(dt_range)]:

    # Ajout dans la liste des combinaison
    dist_actuelle=Distance(choix_actuel,distances_tab,n)
    if dist_actuelle<dist_enregistre:

        choix_enregistre=copy.deepcopy(choix_actuel)
        dist_enregistre=dist_actuelle

    #combi.append(choix_actuel)
    ##print(choix_actuel)
    ##print(dist_actuelle,dist_enregistre)
    print(chiffres_restant)
    choix_actuel,chiffres_restant=Combinaison(choix_actuel,chiffres_restant,n)

    compteur+=1



#print("Voici la liste des combinaisons: \n",combi)
print("Plus courte distance et combinaison liee a ceci: ",dist_enregistre,choix_enregistre)
print("nombre de combinaison:",compteur)

fig = plt.figure()
ax = fig.add_subplot(111)
pos=0
for point in pt:
    pos+=1
    plt.plot(point[0], point[1], marker='o', markersize=3, color="red")
    # les ajouts sont des offset
    ax.text(point[0]+min(5,point[0]//100), point[1]+min(5,point[1]//100), str(pos), fontsize=15)

for trace in range(len(choix_enregistre)-1):
    x=(pt[choix_enregistre[trace]-1][0],pt[choix_enregistre[min(trace+1,len(choix_enregistre)-1)]-1][0])
    y=(pt[choix_enregistre[trace]-1][1],pt[choix_enregistre[min(trace+1,len(choix_enregistre)-1)]-1][1])
    plt.plot(x,y)


plt.show()
