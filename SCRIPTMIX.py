from BRUTEFORCE import PlusCourtChemin
from ANTOPTIMIZATION import Fourmis
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

save_document= open("sauvegarde.txt","w+")

points=[]
maxi=20
mini=-maxi
nombre_point=7
# Coordonnees varient entre mini et maxi, generees aleaatoirement.
for k in range(nombre_point):
    points.append((randint(mini,maxi),randint(mini,maxi)))

#points=((1,6),(3,2),(7,5))
print(points)

start=10
end=1101
pas=75
proba_choix=[]
pourc_choix=[]



















pcc=PlusCourtChemin(points)
print("Plus courte distance et combinaison liee a celle-ci:",pcc[0],pcc[1])
print("Nombre de combinaisons de points:",pcc[2])

nombre_tours=int(input("Entrez le nombre de tours effectues par chacune de fourmis (entier naturel): "))
coefficients=(1.5,0.99)

for nombre_fourmis in range(start,end,pas):
    reussite=0
    distance_test=0
    print("NOMBRE DE FOURMIS:",nombre_fourmis)
    for nombre_test in range(10):
        print("numéro du test pour",nombre_fourmis,"fourmis :",nombre_test+1)
        fourmis_chemin=Fourmis(points,nombre_fourmis,nombre_tours,coefficients,5)
        print("Distance calculee cette fois:",fourmis_chemin[0],"\n")
        if fourmis_chemin[0]==pcc[0]:
            reussite+=1
        distance_test+=fourmis_chemin[0]

    proba_choix.append((reussite/(nombre_test+1))*100)
    pourc_choix.append(((nombre_test+1)*pcc[0]/distance_test))




# Sauvegarde resultat
save_document.write("Pourcentage d'obtention du plus court chemin en fonction du nombre de fourmis qui varie entre "+str(start)+" et "+str(end)+" avec un pas de "+str(pas)+". \n On compte "+str(len(points))+" points qui sont respectivement: "+str(points)+". \n On a fait tourner la simulation avec "+str(nombre_tours)+" tour(s) par fourmis \n le nombre de possibilités de combinaisons différentes total est "+str(pcc[2])+".")
save_document.write("\n [")

for l in proba_choix:
    save_document.write(str(l)+" ")

save_document.write("]")
save_document.close()


# Barres
  #fig1 = plt.figure()
  #

  #
  #rects1=plt.bar(pos_x,proba_choix,0.35,1,color='b',label='Pourcentage de + court chemin')
  #plt.xticks(pos_x,)
  #plt.xlabel("Nombre de fourmis")
  #plt.ylabel("Pourcentage")
  #plt.legend()
  #plt.ylim(0,100)
  #
  #plt.title("Pourcentage de réussite de l'algorithme en fonction du nombre de fourmis")
  #
  #plt.show()


pos_x=[x for x in range(start,end,pas)]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

ax1.bar(pos_x,proba_choix,color='cyan',label='Pourcentage de + court chemin')
ax1.set(
title="Pourcentage d'obtention du plus court chemin en fonction du nombre de fourmis",
xlabel="Nombre de fourmis",
ylabel="en %",
ylim=(0,100));

ax2.bar(pos_x,pourc_choix,color='r',label='Indice de distance moyen des chemins')
ax2.set(title = "Indice de réussite en fonction du nombre de fourmis",
       xlabel = "Nombre de fourmis",
       ylabel = "en %",
       ylim=(0,1));




plt.xticks(pos_x,pos_x)
plt.legend()
plt.savefig('chart.png')
plt.show()





os.system("shutdown /s /t 1")


#nombre_fourmis=int(input("Entrez le nombre de fourmis avec lesquelles on lancera la simulation (entier naturel): "))
#
#fourmis_chemin=Fourmis(points,nombre_fourmis,nombre_tours,coefficients,5)
#print("Plus courte distance des fourmis et combinaison liee a celle-ci:",fourmis_chemin[0],fourmis_chemin[1])
