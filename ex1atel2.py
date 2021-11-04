# Initialize a list
L1=[2,7,9,3,7,3,9]
L2=[33,6,25,12,4,6,9]
L3=[]  # on a declaré une 3ème liste pour stocker les éléments qu'on va les exporter depuis les deux listes 
for i in range(1,len(L1),2):   #on a utilisé la boucle 'for' qui va commencer depuis l'indice 1 jusqu'à la fin de la première liste avec deux pas pour qu'il va prendre seulement les éléments avec l'indice impair
    L3.append(L1[i])  #on a utilisé la boucle 'append' pour lorsqu'il trouve un élément avec indice impair il va le stocker dans la 3ème liste
for i in range(0,len(L2),2):  #on a utilisé une autre boucle 'for' comme la précédente , mais maintenant pour les éléments avec indices pairs(la boucle va commencer depuis l'indice 0 cette fois)
    L3.append(L2[i])   #même chose dans la précédente

print(L3)  #ici on va afficher la liste qui contient les éléments avec indices IMPAIRS de la 1ère liste , et les éléments avec indices PAIRS de la 2ème 