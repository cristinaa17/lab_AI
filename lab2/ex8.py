tari_risc = ["coreea de nord", "siria", "iran"]

tranzactii_suspecte = 0

nr_tranzactii = int(input("Câte tranzacții vrei să introduci? "))

print("\nProcesăm tranzacțiile...\n")

if nr_tranzactii > 3:
    print("⚠Posibilă activitate bot (prea multe tranzacții într-un minut)\n")
    tranzactii_suspecte += 1

for i in range(nr_tranzactii):
    print(f"Tranzacția {i + 1}")

    suma = int(input("Suma (RON): "))
    tara = input("Țara: ").strip().lower()

    if tara in tari_risc:
        mesaj = "Frauduloasă (țară cu risc ridicat)"
        tranzactii_suspecte += 1
    elif suma > 10000:
        mesaj = "Suspicioasă (sumă mare)"
        tranzactii_suspecte += 1
    else:
        mesaj = "Sigură"

    print(f"Tranzacție: {suma} RON din {tara.title()} → {mesaj}\n")

if tranzactii_suspecte >= 3:
    print(f"{tranzactii_suspecte} tranzacții suspecte detectate! Cont blocat.")
else:
    print("Contul este sigur.")