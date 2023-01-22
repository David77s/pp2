"""
#losowe elementy zbioru listy

import random

numbers = []

for i in range(10):
    number = random.randint(1,100)
    numbers.append(number)


print(numbers)

"""

#przyklad 10.2


import random

print()


""""
# moja proba zadania 10.2
import random

numbers = []
z = 0
p = 0

for i in range(16):
    number = random.randint(1,6)
    numbers.append(number)
    if number == 6:
        z += 1
    if numbers[i] == numbers[i-1]:
        p += 1

print("Zestaw wylosowanych wyników",numbers)
print("Za ósmym razem wylosowano: ",numbers[7])
print("Liczbę 6 wylosowano: ",z, "razy")
print("Maksymalna liczba wyrzuconych wartości pod rząd to: ",p)

"""

