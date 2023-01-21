#3 = 1 * 2 * 3 = 6

number = 4 #1*2*3*
factorial = 1

#for i in range(1, number + 1):
 #   factorial *= i
#print(factorial)

while number:
    factorial *= number

    print(number,factorial)
    number -= 1