# jak przechowywac wiele wartości - 5 liczb całkowitych

#numbers = [1,1,1,1,1]
#print(numbers)
"""
fruits = ["banan","jabłko","czereśnia",99,True]  #indeksy ujemne od -5,-4,-3,-2,-1
print(fruits)

print(fruits[1])
print(fruits[4],len(fruits))

print(fruits[-1])

# funkcja
l = len(fruits)
print(l)

# metoda
#fruits.append("kiwi")
#print(fruits)

fruits.insert(0,"kiwi")
print(fruits)
"""


""""
# half dollars
# liczba produkcji monet półdolarowych w latach 2012,2013, 2013 w Denver i Filadelfii
denver = [1_700_000,4_600_000,2_100_000]

philadelphia = []

philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

total = [0,0,0]

total[0] = denver[0] + philadelphia[0]
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]

average = (total[0] +total[1]+ total[2] / len(total))


# print("{:,d}".format(total[0]).replace(","," ")) - przejrzysty widok tego poniżej
print("Produkcja w 2012 wyniosła",total[0],"sztuk")
print("Produkcja w 2013 wyniosła",total[1],"sztuk")
print("Produkcja w 2014 wyniosła",total[2],"sztuk")
"""

# iterowanie po listach

# 1 sposób
"""
fruits = ["banan","jabłko", "czereśnia"]

for i in range(len(fruits)):
    print(fruits)
"""
""
fruits = ["banan","jabłko", "czereśnia"]
for f in fruits:
    print(f)
"""