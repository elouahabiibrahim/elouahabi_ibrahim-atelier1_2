# Function that Sort by insertion 

def tri_selection(tab):
    for i in range(len(tab)):

        min = i

        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp

    return tab

tab = [4,76,66,4,9,8,41,0]

tri_selection(tab)

print("le tab est :")
for i in range(len(tab)) :
    print("%d" % tab[i])
    


