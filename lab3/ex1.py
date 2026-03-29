def determina_castigator(j1, j2):
    if j1 == j2:
        return "egal"
    elif (j1 == "piatra" and j2 == "foarfeca") or \
            (j1 == "foarfeca" and j2 == "hartie") or \
            (j1 == "hartie" and j2 == "piatra"):
        return "jucator1"
    else:
        return "jucator2"


def joc():
    while True:
        print("\n Joc Piatra-Hartie-Foarfeca ")

        j1 = input("Jucatorul 1 alege (piatra/hartie/foarfeca): ").lower()
        j2 = input("Jucatorul 2 alege (piatra/hartie/foarfeca): ").lower()

        optiuni = ["piatra", "hartie", "foarfeca"]

        if j1 not in optiuni or j2 not in optiuni:
            print("Alegere invalida! Incearca din nou.")
            continue

        rezultat = determina_castigator(j1, j2)

        if rezultat == "egal":
            print("Este egalitate!")
        elif rezultat == "jucator1":
            print(" Felicitari! Jucatorul 1 castiga!")
        else:
            print(" Felicitari! Jucatorul 2 castiga!")

        din_nou = input("Doriti sa jucati din nou? (da/nu): ").lower()
        if din_nou != "da":
            print("Paaaa!")
            break

joc()