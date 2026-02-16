def jkadd(a, b):
    return a + b
def jksub(a, b):
    return a - b
def jkmul(a, b):
    return a * b
def jkdiv(a, b):
    if b == 0:
        return "Fehler: Division durch 0!"
    return a / b
#def jkmmittelwert(a, b):
#    return (a + b)/2
def jkmittelwert(liste):
    if not liste:  # Prüfen, ob die Liste leer ist
        return 0
    return sum(liste) / len(liste)
