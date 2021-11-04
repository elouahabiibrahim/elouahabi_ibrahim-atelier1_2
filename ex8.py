#fonction pour trouver la fréquence d’un caractère dans une chaîne
def fréquence(m,c) :
    comp=0
    for x in m :
        if x==c :
            comp+=1
    return comp    

m= "bonjour"
cara=input("tape un caractère  ")
# affichage du resultat final
print (fréquence(m,cara))