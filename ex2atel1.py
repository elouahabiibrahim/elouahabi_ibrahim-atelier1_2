# Fonction convertir le nombre en binaire inversédef conver(B) :
def conver(B) :
    F = 1
    NB = 0
    while B != 0 :
    
        R = B % 2
        NB += R * F
        F *= 10
        B //= 2
    return NB

x = int (input("saisir un nombre :  "))
# affichage du resultat final
print ("Votre nombre  binaire est :" )
print (conver(x))

    

