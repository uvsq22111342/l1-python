import time


def tempsEnSecondes(temps):
    """ Renvoie la valeur en seconde de temps donné comme\
    jour, heure, minute, seconde."""
    return temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]  


def secondeEnTemps(secondes):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond \
        au nombre de seconde passé en argument"""
    j = secondes // (24 * 3600)
    h = secondes % (24 * 3600) // 3600
    min = (secondes % (24 * 3600)) % 3600 // 60
    secondes = (secondes % (24 * 3600)) % 3600 % 60
    return (j, h, min, secondes)


def afficheTemps(temps):
    """ Renvoie l'affichage du temps """
    if temps[0] == 1:
        print(temps[0], "jour, ", end="")
    elif temps[0] > 1:
        print(temps[0], "jours, ", end="")
    if temps[1] == 1:
        print(temps[1], "heure, ", end="")
    elif temps[1] > 1:
        print(temps[1], "heures, ", end="")
    if temps[2] == 1:
        print(temps[2], "minute, ", end="")
    elif temps[2] > 1:
        print(temps[2], "minutes, ", end="")
    if temps[3] == 1:
        print(temps[3], "seconde, ", end="")
    elif temps[3] > 1:
        print(temps[3], "secondes, ", end="")


def demandeTemps():
    j = input("Taper un nombre de jours ")
    h = input("Taper un nombre d'heures ")
    while int(h) >= 24:
        h = input("Taper un nombre d'heures ")
    m = input("Taper un nombre de minutes ")
    while int(m) >= 60:
        m = input("Taper un nombre de minutes ")
    s = input("Taper un nombre de secondes")
    while int(s) >= 60:
        s = input("Taper un nombre de secondes ")
    return(int(j), int(h), int(m), int(s))


def sommeTemps(temps1, temps2):
    return secondeEnTemps(tempsEnSecondes(temps1) + tempsEnSecondes(temps2))


def proportionTemps(temps=(0, 0, 0, 0), proportion=0.1):
    return secondeEnTemps(tempsEnSecondes(temps) * proportion)


def tempsEndate(temps):
    ans = 1970 + (temps[0] // 365)
    jour = temps[0] % 365
    h = temps[1]
    m = temps[2]
    s = temps[3]
    return (ans, jour, h, m, s)


def afficheDate(temps):
    t = temps
    if t[1] < 31:
        print(t[1], "Janvier", end="")
    elif t[1] < 59:
        print(t[1] - 31, "Février", end="")
    elif t[1] < 90:
        print(t[1] - 59, "Mars", end="")
    elif t[1] < 120:
        print(t[1] - 90, "Avril", end="")
    elif t[1] < 151:
        print(t[1] - 120, "Mai", end="")
    elif t[1] < 181:
        print(t[1] - 151, "Juin", end="")
    elif t[1] < 212:
        print(t[1] - 181, "Juillet", end="")
    elif t[1] < 242:
        print(t[1] - 212, "Août", end="")
    elif t[1] < 273:
        print(t[1] - 242, "Septembre", end="")
    elif t[1] < 303:
        print(t[1] - 273, "Octobre", end="")
    elif t[1] < 334:
        print(t[1] - 303, " Novembre", end="")
    elif t[1] < 364:
        print(t[1] - 334, "Décembre", end="")
    print("", t[0], "à", t[2], ":", t[3], ": ", t[4])


def bisextile(jour):
    ans = jour // 365
    for i in range(ans + 1):
        if (1970 + i) % 4 == 0 and ((1970 + i) % 100 != 0 or
                                    (1970 + i) % 400 == 0):
            print(1970 + i, ", ", end="")


def nombreBisextile(jour):
    n = 0
    ans = jour // 365
    for i in range(ans + 1):
        if (1970 + i) % 4 == 0 and ((1970 + i) % 100 != 0 or (1970 + i) % 400 == 0):
            n += 1
    return n


def tempsEnDateBisextile(temps):
    t = tempsEnSecondes(temps)
    t = secondeEnTemps(t)
    b = nombreBisextile(t[0])
    ans = 1970 + temps[0] // 365
    jour = temps[0] % 365 - b
    return (ans, jour, temps[1], temps[2], temps[3])


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
print(time.gmtime())


def verifie(liste_temps):
    for i in range(len(liste_temps)):
        S = 0
        L = liste_temps[i]  
        for j in range(4):
            if L[j] <= 48:
                S = S + L[j]
            else:
                print("L'employé a travaillé ", L[j] - 48, "heures de trop\
                     dans la semaine", j + 1, "du mois", i)
                S = S + L[j]
        if S > 140:
            print("L'employé a travaillé", S - 140, "heures en trop\
                 dans le mois", i + 1)


liste_temps = [[1, 2, 39, 34], [0, 1, 9, 4], [0, 29, 39, 51], [0, 31, 13, 46], [50, 50, 50, 50]]
verifie(liste_temps) 