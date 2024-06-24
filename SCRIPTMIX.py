from BRUTEFORCE import PlusCourtChemin
from ANTOPTIMIZATION import Fourmis
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

import time


save_document= open("sauvegarde_indice.txt","a")

points=[]
maxi=20
mini=-maxi
nombre_point=8
# Coordonnees varient entre mini et maxi, generees aleaatoirement.
for k in range(nombre_point):
    points.append((randint(mini,maxi),randint(mini,maxi)))

#points=((1,6),(3,2),(7,5))
print("points: ",points)

start=10
end=6011
pas=700
proba_choix=[]
pourc_choix=[]
temps_calcul=[]

debut_temps = time.time()
pcc=PlusCourtChemin(points)
fin_temps= time.time()

pcc_temps=fin_temps-debut_temps
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

        if nombre_test==0:
            start_time = time.time()

        fourmis_chemin=Fourmis(points,nombre_fourmis,nombre_tours,coefficients,5)

        if nombre_test==0:
            end_time = time.time()
            print("Temps pour un test avec ",nombre_fourmis," fourmis: ",end_time-start_time," s.")

        print("Distance calculee cette fois:",fourmis_chemin[0],"\n")
        if fourmis_chemin[0]==pcc[0]:
            reussite+=1
        distance_test+=fourmis_chemin[0]

    temps_calcul.append(end_time-start_time)
    proba_choix.append((reussite/(nombre_test+1))*100)
    pourc_choix.append(((nombre_test+1)*pcc[0]/distance_test))





# Sauvegarde resultat
save_document.write("\n \n \n \nPourcentage d'obtention du plus court chemin en fonction du nombre de fourmis qui varie entre "
+str(start)+" et "+str(end)+" avec un pas de "+str(pas)+". \n On compte "+str(len(points))+" points qui sont respectivement: "+str(points)+"."
" Le nombre de possibilités de combinaisons possibles est donc de "+str(pcc[2])+". \n"
"On a fait tourner la simulation avec "+str(nombre_tours)+" tour(s) par fourmis. \nles coefficient étaient "+str(coefficients[0])+" et "+str(coefficients[1])+".")


save_document.write("\nles Pourcentage d'obtention du plus court chemin étaient respectivement: [")

for l in proba_choix:
    save_document.write(str(l)+" ")

save_document.write("] \n")


save_document.write("les indices de réussite étaient respectivement: [")

for p in pourc_choix:
    save_document.write(str(p)+" ")

save_document.write("] \n")

save_document.write("Les temps de calcul (en s) nécessaires étaient respectivement: : [")

for c in temps_calcul:
    save_document.write(str(c)+" ")

save_document.write("] \n le temps mis par l'algorithme exact etait: "+str(pcc_temps)+"s.")

save_document.close()


pos_x=[j for j in range(start,end,pas)]

fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(18, 18))

ax1.bar(pos_x,proba_choix,color='cyan')
ax1.set(
title="Obtention du + court chemin en fonction du nombre de fourmis",
xlabel="Nombre de fourmis",
ylabel="en %",
ylim=(0,100));

ax2.bar(pos_x,pourc_choix,color='r')
ax2.set(title = "Indice de réussite en fonction du nombre de fourmis",
       xlabel = "Nombre de fourmis",
       ylabel = "en %",
       ylim=(0,1));

#ax3.bar(pos_x,temps_calcul,color='yellow')
ax3.set(title = "Temps de calcul pour un test",
       xlabel = "Nombre de fourmis",
       ylabel = "en s");


for trace in range(len(temps_calcul)-1):
    x=(pos_x[trace],pos_x[min(trace+1,len(temps_calcul)-1)])
    y=(temps_calcul[trace],temps_calcul[min(trace+1,len(temps_calcul)-1)])
    plt.plot(x,y)

#plt.xticks(pos_x,pos_x)

#plt.xticks(pos_x,pos_x)

plt.savefig('chart2.png')
#os.system("shutdown /s /t 1")
#plt.show()








#nombre_fourmis=int(input("Entrez le nombre de fourmis avec lesquelles on lancera la simulation (entier naturel): "))
#
#fourmis_chemin=Fourmis(points,nombre_fourmis,nombre_tours,coefficients,5)
#print("Plus courte distance des fourmis et combinaison liee a celle-ci:",fourmis_chemin[0],fourmis_chemin[1])
