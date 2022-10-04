

def syracuse(n):
    L = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            L.append(n)
        else:
            n = 3*n + 1
            L.append(n)
    return L


def testeConjecture(n_max):
    for i in range(1, n_max + 1):
        if syracuse(i)[-1] != 1:
            return False
    return True


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n)) - 1


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    L = [tempsVol(i) for i in range(1, n_max + 1)]
    return L


def altitude(n):
    a = 1
    for i in range(1, n + 1):
        if max(syracuse(i)) > a:
            a = max(syracuse(i))
            b = i
    return a, b

print(altitude(10000))
