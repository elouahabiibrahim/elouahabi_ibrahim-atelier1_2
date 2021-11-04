# Initialize a list
Set1={8,6,7,11,4,6,3,5,8,56}
Set2={1,4,56,5,11,6,8}

# Intersection operation
Set3=Set1.intersection(Set2)  #cette set3 est le résultat de l'intersection de la set1 avec set2, on a utilisé l'operation : set1.intersection(set2) 
print(Set3)  #on a afficher set3

# Symmetric Difference Operation
print(Set1.difference(Set3))  #on a utilisé l'opération suivante : set1.difference(set2) pour supprimer les éléments communs entre la set1 et set2 de la set1  

   