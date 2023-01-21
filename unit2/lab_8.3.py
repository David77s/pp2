s = 0
for i in range(64):
    s += 2 ** i
print("Suma wszystkich ziaren zboża na szachownicy: " + str(s))

# 1 ziarno = 0,4 mg
# 1 ziarno = 0,0004 g

# 1 kg = 1000g
# 1t = 1000 kg

tons = int(s * 0.0004 / 1000 / 1000)
print(tons)

# produkcja pszenicy na świecie to około 782 mln ton

years = round(tons / 782e6, 2)
print(years)

# 1 pociąg może transportować 2200 ton

trains = int(tons/2200) + 1
print(trains)
