from math import *
from random import randint
pt=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
n=len(pt)
d_terme=n-3

def Empty_List(n):
    """créer une double liste (matrice carrée) nulle de taille n (entier naturel >=3)"""
    inside=[[0 for j in range(n )] for i in range(n)]
    return inside

def Reset(chiffres_restant,a_partir_de,choix_actuel,n):

    """ chiffres_restant: tableau
    a_partir_de: int (entier naturel)
    choix_actuel: liste (combinaison actuelle)
    Permet de réinitialiser les choix possibles pour les nombres après un certain rang (a_partir_de)"""

    for j in range(a_partir_de+1,n-2):
        print("je suis j",j)
        chiffres_restant[j]=[p for p in range(2,n+1)]

        # Enlever éléments déjà utilisés avant
        print("Deux instances:",a_partir_de+1,n-2)
        print(chiffres_restant[j])
        for m in range(0,j):
            chiffres_restant[j].remove(choix_actuel[m])
        print(chiffres_restant[j])


    print(chiffres_restant)
    return chiffres_restant



def Combinaison(n):
    """"""
    # Ensemble des cominaisons à renvoyer
    combi=[]

    # servira pour créer les combinaisons
    chiffres_restant=[[j for j in range(2,n+1)] for x in range(n-2)]

    # Permettra d'Initialiser la première combinaison sans répéter
    choix_possible=[j for j in range(2,n+1)]

    choix_actuel=[]

    # INITIALISATION! REFAIRE APRES SIMILAIRE
    for m in range(n-2):
        # Initiliasation première (aléatoire dans choix_possible)
        choix=choix_possible[randint(0,len(choix_possible)-1)]

        # Ajoute au choix actuel
        choix_actuel.append(choix)

        # Enlève de la liste dans laquel on choisira les prochains chiffres
        choix_possible.remove(choix)

        # minimum évite de dépasser si on est au dernier terme
        for apres in range(min(m+1,n-2),n-2):
            chiffres_restant[apres].remove(choix)






    while chiffres_restant[0]!=[]:
        # Ajoute la nouvelle combinaison et enlève celle actuelle des possiblités encore envisagable
        print(choix_actuel)
        print(chiffres_restant)

        combi.append(choix_actuel)
        chiffres_restant[d_terme].remove(choix_actuel[d_terme])


        if chiffres_restant[d_terme]!=[]:
            choix_actuel[d_terme]=chiffres_restant[d_terme][randint(0,len(chiffres_restant[d_terme])-1)]
        else:
            for compteur in range(0,n-2):
                #Vérifié qu'on puisse continuer
                if chiffres_restant[d_terme-compteur]!=[]:

                    choix_actuel[d_terme-compteur]=chiffres_restant[d_terme-compteur][randint(0,len(chiffres_restant[d_terme-compteur])-1)]

                    chiffres_restant[d_terme-compteur].remove(choix_actuel[d_terme-compteur])

                    # RESET ceux d'après
                    chiffres_restant=Reset(chiffres_restant,d_terme-compteur,choix_actuel,n) #<-- marche pas encore
                    # Sort de toutes les boucles
                    break
                    break
                    break


    return(combi)

print("D'accord:",Combinaison(n))


distance=Empty_List(n)

# Création de la matrice comportant les distances
for i in range(n):
    for j in range(n):
         #if i !=j:
        distance[i][j]=int(sqrt(((pt[i][0]-pt[j][0])**2)+(pt[i][1]-pt[j][1])**2))


# Affiche la matrice
#for i in range(n):
#    print([distance[i][j] for j in range(n)])
