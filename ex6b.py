#tri bulle 
def tri_bulle(tab):
    n = len(tab)

    for i in range(n):
        for j in range(0, n - i - 1):

            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


tab = [7,7,9,1,0,3,55,46,77,98,99]

tri_bulle(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])
