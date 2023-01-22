# Xql
#dla każdego znaku zmieniono 4 bit na przeciwny
#bity liczymy od najmniej znaczacego, 4 bit bedzie mial indeks 3

#print(ord("c")) # wartosc c w tabeli ascii
#print(bin(ord("c"))) # c binarnie

#print(chr(99)) # konwerowanie z liczby na znak c

#print("{:08b}".format(ord("c"))) # c na 8 bitach

# 01100011 - nasza liczba
# 00001000 - maska
# 01101011 - używamy XORa ( alternatywa rozłączna), aby dojść do zamiany za pomocą maski


#print("{:08b}".format(ord("c") ^ (1 << 3)))

#print(chr(ord("c") ^ (1 << 3)))

ms = "Xql`gf(bm{|(nibfq)"
for c in ms:
    print(chr(ord(c) ^ (1 << 3)), end="")