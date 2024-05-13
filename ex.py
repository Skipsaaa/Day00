import random
ma_liste = [random.randit(1,10) for _ in range(5)]
print(ma_liste)
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j]> liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
tri_bulles(ma_liste)

print("dans l'ordre")
for num in ma_liste:
    print(num)            