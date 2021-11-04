L=[1,5,9,34,2,7,13] #La liste
L1=[] # Le nouveaux liste pour stoker les elements existe dans le dictionaire 
DIC={"Salim":34 , "Fakhita":9 , "Abd elhamid":13 , "Zolikha":1} #Le dictionaire

for val in L: #Boucle for pour passe dans la liste
        if val in DIC.values():
            L1.append(val) #Remplier les elements de l'exestante dans le liste
    

print(L1) #Affichage de liste de resultat


