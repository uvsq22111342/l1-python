

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
