""""
# Jeżeli temperatura będzie dodatnia  albo będzie słonecznie
# to poójdziemy na spacer, a jeżeli nie to zostaniemy w domu

temperature = 12
is_sun_shining = False

if temperature > 0 or is_sun_shining: #True or False = True
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")


# Jeżeli temperatura będzie ujemna lub będzie pochmurno to zostaniemy w domu a jezeli nie to pojdziemy na spacer

temperature = -1
is_sun_shining = False


if temperature < 0 or not is_sun_shining:
    print("Zostajemy w domu")
else:
    print("Idziemy na spacer")

# and - koniunkcja, czytamy jako i
# or - alternatywa, czytamy jako lub
# not - negacja, czytamy jak nie


#wyświetl cyfrę, chyba że...
#liczba parzysta lub liczba większa od 6 to wyswietl gwiazdkę

for i in range(10):
    if i % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)
"""


