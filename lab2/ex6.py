import random

inventar = []

print("🌲 Bine ai venit în pădurea magică!")
print("Trebuie să alegi o direcție: stanga sau dreapta")

directie = input("Încotro mergi? ").strip().lower()

if directie == "stanga":
    print("\nMergi spre stânga...")

    eveniment = random.choice(["lup", "comoara"])

    if eveniment == "lup":
        print("Te întâlnești cu un lup!")
        actiune = input("Fugi sau lupti? ").strip().lower()

        if actiune == "fug":
            print("Ai scăpat cu bine!")
        elif actiune == "lupt":
            print("Ai învins lupul! Găsești o sabie.")
            inventar.append("sabie")
        else:
            print("Nu ai ales corect!")

    elif eveniment == "comoara":
        print("Ai găsit o comoară!")
        inventar.append("aur")

elif directie == "dreapta":
    print("\nMergi spre dreapta...")

    eveniment = random.choice(["vrajitor", "fantana"])

    if eveniment == "vrajitor":
        print("Întâlnești un vrăjitor.")
        raspuns = input("Vrei o poțiune? (da/nu) ").strip().lower()

        if raspuns == "da":
            print("Primești o poțiune magică!")
            inventar.append("poțiune")
        elif raspuns == "nu":
            print("Vrăjitorul dispare...")
        else:
            print("Răspuns invalid!")

    elif eveniment == "fantana":
        print("Găsești o fântână misterioasă.")
        print("Primești un scut!")
        inventar.append("scut")

else:
    print("Nu ai ales corect direcția... Te-ai rătăcit!")

print("\nInventarul tău:", inventar)