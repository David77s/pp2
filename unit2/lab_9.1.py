#zadanie 1

x = int(input("Wprowadż pierwszą cyfrę ze zbioru "))
y = int(input("Wprowadż ostatnią cyfrę ze zbioru "))

for num in range(x, y +1 ):
    if num % 3 == 0 or num % 5 == 0 or num % 7 ==0:
        print(num)