# zadanie 1

"""
x = int(input("Wprowadż pierwszą cyfrę ze zbioru "))
y = int(input("Wprowadż ostatnią cyfrę ze zbioru "))


for i in range(x, y+1):
    if (x % 3 == 0 or y % 3 == 0) and (x % 5 == 0 or y % 5 == 0) or (x % 7 == 0 or y % 7 ==0):
        print(i)

"""
#1 wersja

"""""   
 range_from = int(input("Wprowadż pierwszą cyfrę ze zbioru "))
 range_to = int(input("Wprowadż ostatnią cyfrę ze zbioru "))

for number in range(range_from, range_from +1 ):
    if number % 3 == 0 or number % 5 == 0 or number % 7 ==0:
        print(number)
"""
"""
#2 wersja
print("Podaj zakres liczb")
range_from = int(input("od "))
range_to = int(input("do "))

print("Liczby z zakresu od", range_from, "do", range_to, "podzielone przez 3 lub 5 lub 7 to")

for number in range(range_from,range_to+1):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        if not is_first:
            print(",", end=",")
        print(number, end=",")
        is_first = False
print(",")
"""
"""
a =3
b = 4
c = 7

print(a < b < c)
print(a < b and b <c)

"""