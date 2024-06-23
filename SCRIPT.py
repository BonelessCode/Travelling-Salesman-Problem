from math import *
from random import randint
from copy import deepcopy
pt=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
n=len(pt)
d_terme=n-2
dt_range=n-1

def Empty_List(n):
    """créer une double liste (matrice carrée) nulle de taille n (entier naturel >=3)"""
    inside=[[0 for j in range(n )] for i in range(n)]
    return inside


def Dernier_Terme(chiffres_restant,dt_range):
    """"""
    p_max_test=0
    for compteur_test in range(0,dt_range):
        # Cherche la dernière liste non vide
        if chiffres_restant[compteur_test]!=[]:
            p_max_test=compteur_test

    return p_max_test

# Ensemble des cominaisons à renvoyer
combi=[]
backup=0
pos_max=4

# servira pour créer les combinaisons
chiffres_restant=[[j for j in range(2,n+1)] for x in range(dt_range)]
choix_actuel=[0 for i in range(dt_range)]

# Construction de la première Combinaison choisie
for j in range(dt_range):
    #choix_actuel[j]=chiffres_restant[j][randint(0,len(chiffres_restant[j])-1)]

    choix_actuel[j]=chiffres_restant[j][0]

    # Enlève les chiffres déjà utilisés pour les combinaisons suivantes et empêche de dépasser le dernier terme du range
    for m in range(min(j+1,dt_range),dt_range):
        chiffres_restant[m].remove(choix_actuel[j])


while chiffres_restant[0]!=[]:
    print(choix_actuel)
    print(chiffres_restant)

    if backup != choix_actuel:
        combi.append(choix_actuel)
        backup=deepcopy(choix_actuel)



    # S'assurer que l'ensemble est toujours non vide
    pos_max=Dernier_Terme(chiffres_restant,dt_range)

    # Rafraichissement des données
    choix_actuel[pos_max]=chiffres_restant[pos_max][0]
    chiffres_restant[pos_max].remove(choix_actuel[pos_max])


    # Reinitialisaition des valeurs possibles pour les chiffres suivants
    # Permet de compenser les vides
    for k in range(pos_max+1,dt_range):
        chiffres_restant[k]=[o for o in range(2,n+1)]
        print(k,"numero")
        for j in range(0,k):
            chiffres_restant[k].remove(choix_actuel[j])

        choix_actuel[k]=chiffres_restant[k][0]
        print(choix_actuel[k],"valeur")



nb_resultat=len(combi)
print(nb_resultat)
print(combi)
distance=Empty_List(n)

# Création de la matrice comportant les distances
for i in range(n):
    for j in range(n):
         #if i !=j:
        distance[i][j]=int(sqrt(((pt[i][0]-pt[j][0])**2)+(pt[i][1]-pt[j][1])**2))


# Affiche la matrice
#for i in range(n):
#    print([distance[i][j] for j in range(n)])
