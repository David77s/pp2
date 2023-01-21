a = int(input("Podaj liczbę punktów uzyskanych na kolokwium: "))

if a > 95:
    print("Otrzymujesz ocenę 5")
elif a > 84:
    print("Otrzymujesz ocenę 4.5")
elif a >= 70 :
    print("Otrzymujesz ocenę 4")
elif a > 60 :
    print("Otrzymujesz ocenę 3.5")
elif a > 50:
    print("Otrzymujesz ocenę 3")
else:
    print("Niestety otrzymujesz ocenę niedostateczną")