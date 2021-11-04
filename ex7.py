# Fonction simple qui inverse une chaîne 
#[début : fin : pas] <- avec des pas négatifs on devrait inverser la liste
def Inverse(X):
    print(X[::-1])


chain=str(input("donner votre chain : "))
# Impression du dernier résultat
print(Inverse(chain))