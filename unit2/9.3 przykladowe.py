# 0 1 0 0 1 - przykładowa liczba
# wartosc bitu zerowego to maska:
# 0 0 0 0 1 - maska
#więc and (&)
# 0 0 0 0 1 (wynik czyli 1)

number = int(input("Podaj liczbę "))
n = int(input("Podaj numer bitu "))

mask = 1 << n
result = number & mask

bit = int(bool(result))
print("Bit na pozycj",n,"dla liczby", number,"wynosi",bit)

#sprawdzenie
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(result))

