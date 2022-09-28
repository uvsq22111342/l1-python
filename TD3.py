

def tempsEnSecondes(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]  


def secondeEnTemps(secondes):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = secondes // (24 * 3600)
    h = secondes % (24 * 3600) // 3600
    min = (secondes % (24 * 3600)) % 3600 // 60
    secondes = (secondes % (24 * 3600)) % 3600 % 60
    return (j, h, min, secondes)


temps = secondeEnTemps(342094)
print(type(temps))
print(tempsEnSecondes(temps))
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


def afficheTemps(temps):
    """ Renvoie l'affichage du temps """
    if temps[0] == 1:
        print(temps[0], "jour, ", end = "")
    elif temps[0] > 1:
        print(temps[0], "jours, ", end = "")
    if temps[1] == 1:
        print(temps[1], "heure, ", end = "")
    elif temps[1] > 1:
        print(temps[1], "heures, ", end = "")
    if temps[2] == 1:
        print(temps[2], "minute, ", end = "")
    elif temps[2] > 1:
        print(temps[2], "minutes, ", end = "")
    if temps[3] == 1:
        print(temps[3], "seconde, ", end = "")
    elif temps[3] > 1:
        print(temps[3], "secondes, ", end = "")



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



afficheTemps(demandeTemps())