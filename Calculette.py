Valeur1 = float(input())
Valeur2 = float(input())
Signe = input()

def addition (Valeur1, Valeur2):
    return Valeur1 + Valeur2
def soustraction (Valeur1, Valeur2):
    return Valeur1 - Valeur2
def multiplication (Valeur1, Valeur2):
    return Valeur1 * Valeur2
def division (Valeur1, Valeur2):
    return Valeur1 / Valeur2

if Signe == "+":
    print (addition (Valeur1, Valeur2))
elif Signe == "-":
    print (soustraction (Valeur1, Valeur2))
elif Signe == "*":
    print (multiplication (Valeur1, Valeur2))
else:
    print (division (Valeur1, Valeur2))
