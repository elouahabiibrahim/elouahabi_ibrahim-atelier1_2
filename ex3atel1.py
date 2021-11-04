# Fonction qui détermine la somme des nombres
def SOMME(N):
    # Critères de fin de récursivité (Fin de récursivité)
    if N==0: 
        return 0
    else:
        # Boucle de récursivité
        return N+SOMME(N-1)

n=int(input("Entrez un nombre :  "))
# Impression du résultat final
print("votre somme est :  ")
print(SOMME(n))

       