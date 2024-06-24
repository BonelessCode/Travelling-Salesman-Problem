from math import *
from random import randint
import numpy as np
from random import *
import statistics

import colorama
colorama.init()



def move_cursor(x,y):
    print ("\x1b[{};{}H".format(y+1,x+1))

def clear():
    print ("\x1b[2J")


from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')

def Reguler(extremum_liste,point_actuel,choix_restant,tableau_ou_liste,mini=0):
    """
    Régule les probabilités afin de suivre les phéromones, la distance et d'obtenir un total de 100%"""
    #verifie si on a affaire a un tableau ou une liste

    # Si tableau alors on prends les éléments liés au point sur lequel on est
    if isinstance(tableau_ou_liste[0],list)==True:
        tableau_restant=[tableau_ou_liste[point_actuel-1][x-1] for x in choix_restant]
    # Si liste, alors on utilise directement cette liste
    else:
        tableau_restant=tableau_ou_liste

    # Choix du minimum: Obtient les coefficients en divisant le mini par les éléments
    if mini==1:
        coeff_liste=[extremum_liste/m for m in tableau_restant]
    # Choix du maximum: Obtient les coefficients en divisant par le maxi
    else:
        coeff_liste=[m/extremum_liste for m in tableau_restant]

    coefficient_final=sum(coeff_liste)
    proba_min=solve((coefficient_final*x)-1,x)[0]

    proba_dist=[proba_min*p for p in coeff_liste]

    # Conversion en pourcentage
    proba_dist=[100*a for a in proba_dist]

    # Arrondis les valeurs
    for m in range(len(proba_dist)):
        proba_dist[m]=floor(proba_dist[m])

    # Fais en sorte de toujours atteindre 100
    if sum(proba_dist)!=100:
        proba_dist[0]=int(proba_dist[0]+100-sum(proba_dist))

    return proba_dist

def PlusCourtPlusLong(point_actuel,choix_restant,tableau,long=0):
    """Renvoie le plus court élément de la liste d'indice 1 à partir du deuxième (de la liste) ou
    et le plus long si on ajoute le premier paramètre supplémentaire. Ne prend pas en compte le
    Renvoie aussi l'indice de cet élément en deuxième position"""
    pos=point_actuel-1

    if long==0:
        seuil=max(tableau[point_actuel-1])
        for x in range(len(choix_restant)):
            if tableau[point_actuel-1][choix_restant[x]-1]<seuil and tableau[point_actuel-1][choix_restant[x]-1]!=0:
                seuil=tableau[point_actuel-1][choix_restant[x]-1]
                pos=x
    else:
        seuil=min(tableau[point_actuel-1])
        for x in range(len(choix_restant)):
            if tableau[point_actuel-1][choix_restant[x]-1]>seuil:
                seuil=tableau[point_actuel-1][choix_restant[x]-1]
                pos=x
    return seuil

def Determiner(choix_possibles,chiffre_combi,tableau,n):
    chiffre1=1
    compt2=0
    while choix_possibles!=[]:

        premier_choix=0
        restric=[]
        compteur=0

        compt2+=1
        if compt2==500:
            print("error recurs 2 : \n")
            exit()
        while (premier_choix not in choix_possibles):
            restric.append(premier_choix-1)
            maximum_liste=1
            for k in range(len(tableau[chiffre1-1])):
                if (k not in restric) and (tableau[chiffre1-1][k]>=maximum_liste):
                    maximum_liste=tableau[chiffre1-1][k]
                    pos_max=k
            premier_choix=pos_max+1





            compteur+=1
            if compteur==500:

                print("error recurs : \n")
                print("le choix actuel etait:",chiffre1)
                print("valeur maximale du choix et sa pos: ",tableau[chiffre1-1][k],k)

                print("choix restants:",choix_possibles)
                for h in tableau:
                    print(h)
                print("liste de restriction:",restric)
                exit()













#            maximum_choix=max([tableau[chiffre1-1][f] for f in range(len(tableau[chiffre1-1])) if (f not in restric)])
#            print(chiffre1)
#            print(tableau[chiffre1-1])
#            print("liste des restrictions",restric)




        chiffre_combi.append(premier_choix)
        choix_possibles.remove(premier_choix)
        chiffre1=premier_choix

    return chiffre_combi

#cho=[2,3,4]
#pheromones_spec=[[1,98,6],[98,1,56],[6,56,1]] # 1 2 3
#phero_spec2=[[],[],[],[]]
#print(Determiner(cho,[1],phero_spec2,4)+[1])








def Distance_totale(combi,tableau_pos,n):
    """Renvoie la distance totale de la combinaison"""
    distance_totale=0
    for compt in range(n):
        distance_totale+=tableau_pos[combi[compt]-1][combi[compt+1]-1]

    return distance_totale

def Fourmis(pt,nb_fourmis,nb_tours,coeff,mediane_taille):

    n=len(pt)

    distances_tab=[[0 for j in range(n)] for i in range(n)]
    pheromones_tab=[[1 for j in range(n)] for i in range(n)]


    # Creation de la matrice comportant les distances
    for i_1 in range(n):
        for j_1 in range(n):
             # j lignes et i colonnes
            distances_tab[i_1][j_1]=int(sqrt(((pt[i_1][0]-pt[j_1][0])**2)+(pt[i_1][1]-pt[j_1][1])**2))


    mediane_tab=[]
    coefficient_phero_ajout,coefficient_phero_disp=coeff

    #print(PlusCourtPlusLong(1,[k for k in range(2,n+1)],distances_tab,0,4)[1])

    combinaison_gagnante=[]

    for fourmi_actuelle in range(nb_fourmis):
        for tour_actuel in range(nb_tours):
            point_actuel=1
            choix_restant=[k for k in range(2,n+1)]
            distance_tour=0
            combinaison=[1]

            while choix_restant!=[]:
                dist_mini=PlusCourtPlusLong(point_actuel,choix_restant,distances_tab)
                phero_maxi=PlusCourtPlusLong(point_actuel,choix_restant,pheromones_tab,1)

                proba_dist_tab=Reguler(dist_mini,point_actuel,choix_restant,distances_tab,1)
                proba_phero_tab=Reguler(phero_maxi,point_actuel,choix_restant,pheromones_tab)

                proba_somme=[]
                for compt in range(len(choix_restant)):
                    for compt2 in range(len(choix_restant)):
                        if compt==compt2:
                            proba_somme.append(proba_dist_tab[compt]+proba_phero_tab[compt2])

                proba_max=max(proba_somme)
                #print(proba_max,proba_somme)

                #proba_overall=Reguler(proba_max,point_actuel,choix_restant,proba_somme)
                #proba_overall_pourcentage=[100*a for a in proba_overall]
                proba_overall_pourcentage=Reguler(proba_max,point_actuel,choix_restant,proba_somme)

                #print("proba distance:",proba_dist_tab,sum(proba_dist_tab,))
                #print("proba pheromones:",proba_phero_tab,sum(proba_phero_tab))
                #print("proba totale en POURCENTAGES :",proba_overall_pourcentage,sum(proba_overall_pourcentage))

                ajout=0
                choix_aleatoire=randint(0,99)
                #print("voici le choix aléatoire")
                #print(choix_aleatoire)

                # Si il y a plus d'un choix possible, choisis aléatoirement
                if len(choix_restant)>1:
                    somme=0
                    point_nouveau=point_actuel
                    for m in range(len(proba_overall_pourcentage)):
                        #print("Nous nous placons entre",somme)
                        if choix_aleatoire in range(somme,somme+proba_overall_pourcentage[m]):
                            #print("choix_restant :",choix_restant)
                            point_nouveau=choix_restant[m]
                            #print("le point actuel a ete choisi aleatoirement ici, et il est:", point_nouveau)
                            break
                        #print("et",somme+proba_overall_pourcentage[m])
                        somme+=proba_overall_pourcentage[m]

                elif len(choix_restant)==1:
                    point_nouveau=choix_restant[0]


                combinaison.append(point_nouveau)

                choix_restant.remove(point_nouveau)

                distance_tour+=distances_tab[point_actuel-1][point_nouveau-1]

                point_actuel=point_nouveau

            # Finition avec le dernier point inariant, 1
            distance_tour+=distances_tab[0][point_actuel-1]
            combinaison.append(1)
            # Si la distance est satisfaisante:
            if len(mediane_tab)<mediane_taille or distance_tour<max(mediane_tab):
                mediane_tab.insert(0,distance_tour)

            # if car on doit verifier quoi qu'il arrive si oui ou non la liste depasse la taille
            if len(mediane_tab)>mediane_taille:
                del mediane_tab[len(mediane_tab)-1]

            #print(mediane_tab)
            mediane_tab.sort()

            for i in range(len(pheromones_tab)-1):
                for j in range(len(pheromones_tab[0])-1):
                    if pheromones_tab[i][j]>1:
                        pheromones_tab[i][j]=max(1,pheromones_tab[i][j]*coefficient_phero_disp)

            if distance_tour<=statistics.median(mediane_tab):
                for m in range(len(combinaison)-1):
                    pheromones_tab[combinaison[m]-1][combinaison[m+1]-1]*=coefficient_phero_ajout
                    pheromones_tab[combinaison[m+1]-1][combinaison[m]-1]=pheromones_tab[combinaison[m]-1][combinaison[m+1]-1]

  ##            for h in pheromones_tab:
  ##                print(h)

    unicite_combi=[k for k in range(2,n+1)]
    combinaison_gagnante=Determiner(unicite_combi,[1],pheromones_tab,n)+[1]

#    for a in pheromones_tab:
#        print (a)
#    print("mediane:",mediane_tab)

    return Distance_totale(combinaison_gagnante,distances_tab,n),combinaison_gagnante
