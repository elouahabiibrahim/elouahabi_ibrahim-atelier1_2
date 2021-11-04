#on déclare une liste et un dictionnaire vide
list=[6,7,4,1,6,1,55,2,2,55,22,98,7]
dic={}

for i in range(len(list)): 
    C=0   #on a fait deux boucles 'for' , une pour exporter les éléments et autre pour trouver est ce qu'il y a un élément égale à un autre
    for j in range(len(list)):   #on a fait deux boucles 'for' , une pour exporter les éléments et autre pour trouver est ce qu'il y a un élément égale à un autre
        if list[j]==list[i]:
            C+=1
        #lorsqu'il trouve 2 éléments égaux, le compteur 'a' va être ajouté par 1, et ainsi de suite  
    dic[list[i]]=C  #ici il va être stocker l'élément avec nombre de fois trouvés répétées dans la liste, dans le dictionnaire , la boucle va être répétée jusqu'à la fin de la liste
print(dic)   #il va afficher le dictionnaire
