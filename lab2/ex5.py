import random

print("Bine ai venit la Loteria Python!")
print("Alege 6 numere între 1 și 49.")

numere_user = []

for i in range(6):
    while True:
        nr = int(input(f"Numărul {i + 1}: "))

        if nr < 1 or nr > 49:
            print("Numărul trebuie să fie între 1 și 49!")
        elif nr in numere_user:
            print("Ai ales deja acest număr!")
        else:
            numere_user.append(nr)
            break

numere_extrase = []
while len(numere_extrase) < 6:
    nr = random.randint(1, 49)
    if nr not in numere_extrase:
        numere_extrase.append(nr)

print("Numere extrase:", numere_extrase)

ghicite = []
for nr in numere_user:
    if nr in numere_extrase:
        ghicite.append(nr)

print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")

if len(ghicite) == 6:
    print("Jackpot!!!")
elif len(ghicite) >= 4:
    print("Felicitări! Ai câștigat un premiu mare!")
elif len(ghicite) >= 3:
    print("Felicitări! Ai câștigat un premiu mic!")
else:
    print("Mai încearcă!")