# zadanie 2

counter = 0
for i in range(1,101):
    if (i % 2 == 0 and i > 90) or (i %2 != 0 and i % 9 == 0):
        counter += 1
        print(i)

print("Podanych liczb jest:",counter, "czyli to prawda")



