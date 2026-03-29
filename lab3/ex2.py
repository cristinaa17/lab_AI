def genereaza_factura(nume_client, **kwargs):
    print("\n===== FACTURA =====")
    print(f"Client: {nume_client}")
    total = 0

    for produs, pret in kwargs.items():
        print(f"{produs}: {pret} RON")
        total += pret

    print(f"TOTAL: {total} RON")
    print("===================\n")

genereaza_factura(
    "Cristina Radulescu",
    paine=5,
    lapte=7,
    mere=9
)