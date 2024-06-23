from math import *
from random import randint
from copy import deepcopy
pt=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
n=len(pt)
d_terme=n-2
dt_range=n-1

def Empty_List(n):
    """creer une double liste (matrice carree) nulle de taille n (entier naturel superieur ou egal a 3)"""
    inside=[[0 for j in range(n )] for i in range(n)]
    return inside


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
        chiffres_restant[pos_max].remove(choix_actuel[pos_max])

        # Recursion
        if chiffres_restant[pos_max]==[]:
            choix_actuel,chiffres_restant=Combinaison(choix_actuel,chiffres_restant,n)

        # Si on en est pas au dernier terme
        if choix_actuel!=-1:
            # Reinitialisaition des valeurs possibles pour les chiffres suivants
            for k in range(pos_max+1,dt_range):
                chiffres_restant[k]=[o for o in range(2,n+1)]
                for j in range(0,k):
                    chiffres_restant[k].remove(choix_actuel[j])

                choix_actuel[k]=chiffres_restant[k][0]


            choix_actuel[pos_max]=chiffres_restant[pos_max][0]

            return choix_actuel,chiffres_restant


    """ If et pas else car on doit pouvoir sortir de la fonction
    en renvoyant les valeurs adequate et donc cette condition doit etre testee apres etre sorti d'une possible plongee recursive"""
    if chiffres_restant==[[] for k in range(dt_range)]:
        # Valeur speciale de choix_actuel permettant de terminer le programme
        return (-1,chiffres_restant)





# Ensemble des cominaisons a renvoyer
combi=[]
pos_max=4

# servira pour creer les combinaisons
chiffres_restant=[[j for j in range(2,n+1)] for x in range(dt_range)]
choix_actuel=[0 for i in range(dt_range)]

# Construction de la premiere Combinaison choisie
for j in range(dt_range):
    choix_actuel[j]=chiffres_restant[j][0]

    # Enleve les chiffres deja utilises pour les combinaisons suivantes et empeche de depasser le dernier terme du range
    for m in range(min(j+1,dt_range),dt_range):
        chiffres_restant[m].remove(choix_actuel[j])

# Valeur que prendra choix_actuel a la fin (vois fonction Combinaison)
while choix_actuel!=-1:
    # Ajout dans la liste des combinaison
    combi.append([1]+choix_actuel+[1])
    print(chiffres_restant)
    choix_actuel=Combinaison(choix_actuel,chiffres_restant,n)[0]

print("Voici la liste des combinaisons: \n",combi)
nb_resultat=len(combi)
print("Nombre de resultats: ",nb_resultat)
distance=Empty_List(n)

# Creation de la matrice comportant les distances
for i in range(n):
    for j in range(n):
         #if i !=j:
        distance[i][j]=int(sqrt(((pt[i][0]-pt[j][0])**2)+(pt[i][1]-pt[j][1])**2))


#Affiche la matrice
print("Tableau des distances entre chaques points:")
for i in range(n):
    print([distance[i][j] for j in range(n)])
