import random

counter = 1
number = random.randint(1,10)
guess = int(input("Zgadnij jaką liczbę mam na myśli(1-10): "))

while number != guess:
    guess = int(input("Nie. To nie ta. Sprobuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się za " + str(counter) + " razem")
