print("Podaj długości trzech bokow ( liczby całkowite): ")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a + b > c and b + c > a and c + a > b):
    print("Z tych odcinków można zbudować trójkąt", end=" ")


    if a == b and a == c and c == b:
        print("rownoboczny", end=" ")
    elif a == b or b == c or c == a:
        print("równoramienny", end=" ")
    else:
        print("różnoramienny", end=" ")

    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        print("prostokątny")
    elif (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (a ** 2 + c ** 2 < b ** 2):
        print("rozwartokątny")
    else:
        print("ostrokątny")
else:
    print("Niestety z tych odcinków nie powstanie trojkąt")

