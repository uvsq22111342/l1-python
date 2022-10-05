

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]

def afficheCarre(carre):
    for i in carre:
        for j in i:
            print(j, end=" ")
        print()


def testLignesEgales(carre):
    L = []
    for i in carre:
        S = 0
        for j in i:
            S += j
        L.append(S)
    for k in L:
        if k != L[0]:
            return -1
    return L[0]


def testColonnesEgales(carre):
    L = []
    for i in range(len(carre[0])):
        S = 0
        for j in range(len(carre)):
            S = S + carre[i][j]
        L.append(S)
    for k in L:
        if k != L[0]:
            return -1
    return L[0]


def testDiagonalesEgales(carre):
    S = 0
    D = 0
    for i in range(len(carre)):
        S += carre[i][i]
        D += carre[len(carre) - 1 - i][len(carre) - 1 - i]
    if S != D:
        return -1
    return S


def estCarreMagique(carre):
    return testColonnesEgales(carre) + testDiagonalesEgales(carre) + testLignesEgales(carre) == 3 * testColonnesEgales(carre)


def estNormal(carre):
    S = set(carre[0])
    for i in range(1, len(carre)):
        S = S | set(carre[i])
    for j in range(1, len(carre)**2 + 1):
        if j not in S:
            return False
    return True



print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))