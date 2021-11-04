# Fonction principale qui obtient le nombre de nombres 
def chiff(N):
    # Recursion End criteria -
    if N ==0:
        return 0
    return 1+chiff(N//10)

x =int(input("Entrez le nombre : "))
# Impression du résultat
print("Le nombre des chiffres est : ")
print(chiff(x))
