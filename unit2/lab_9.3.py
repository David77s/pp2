# zadanie 3

number = int(input("Podaj liczbę "))
n = int(input("Podaj numer bitu "))

mask = 1 << n
result = number & mask

bit = int(bool(result))
print("Bit na pozycj",n,"dla liczby", number,"wynosi",bit)
