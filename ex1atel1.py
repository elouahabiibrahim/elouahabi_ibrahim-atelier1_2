# fonction factorielle
def factorial(a):
    # Critères de fin de récursivité (cela arrêtera la récursivité)
    if a == 1: return a
    # Déterminer la factorielle par récursivité
    return a * factorial(a - 1)

# Fonction principale <== 
def determinate(c):
    # Déclaration de la variable d'accumulateur (résultat final)
    result = 0
    #Déclaration de la boucle principale qui réduit au dernier
    for i in range(1, c + 1):
        result = (factorial(i)/i) + result
    # Résultat final
    return result

# affichage du resultat final
print(determinate(int(input("bonjour taper un nombre \n"))))
