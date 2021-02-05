print("First 50 prime number are")
numberOfPrimes = 0
number = 3
primes = []
while numberOfPrimes < 26:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        # print(chr(ord('A') + numberOfPrimes), number)
        primes.append(number)
        numberOfPrimes += 1
    number += 1
# print(primes, ord("A"))
products = []
# code = "CJQUIZKNOWBEVYOFDPFLUXALGORITHMS"
# code = "THEHEQUICKBROWNFOFOXJEJEJEUMPSOVERTHELAZYDOG"
code = "ABABAABABCDEFGHIIJIJKLLMNOPQRSTUVWXYZ"
for i in range(len(code) -1):
    products.append(primes[ord(code[i]) - 65]*primes[ord(code[i+1]) - 65])
print(" ".join(map(str, products)))