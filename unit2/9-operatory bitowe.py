
""""
a = 5
b = 3

# koniunkcja bitowa, &-ampersant

print(a, "&",b, "=",a&b )

#print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-"* 8)
print("{:08b}".format(a & b))

print("\n")

# alternatywa bitowa,, pipe |

print(a, "|",b, "=",a | b )

#print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-"* 8)
print("{:08b}".format(a | b))

print("\n")


# alternatywa rozłączna xor ^

print(a, "^",b, "=",a ^b )

#print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-"* 8)
print("{:08b}".format(a ^ b))


print("\n")

# przesuniecie bitowe w prawo >>

print(a, ">>",b, "=",a >>b )


print("{:08b}".format(a))
print("{:08b}".format(b))
print("-"* 8)
print("{:08b}".format(a >> b))

print()

# przesuniecie bitowe w lewo <<

print(a, "<<",b, "=",a <<b )


print("{:08b}".format(a))
print("{:08b}".format(b))
print("-"* 8)
print("{:08b}".format(a << b))

print()

#  ~

print("~ "+ str(a), "=",~a )


print("{:08b}".format(a))

print("-"* 8)
print("{:08b}".format(~a))


for i in range(5 -6, -1):
    print("{0:08b} => {1:d}".format(i & 255,i))
"""