# Write your code here :-)
import time
def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3 * number + 1


print("Please enter an integer")
while True:
    cislo = input()
    try:
        cislo = int(cislo)
    except ValueError:
        print("Please enter an integer")
        continue
    break

while cislo != 1:
    time.sleep(0.1)
    cislo = collatz(cislo)
    print(cislo)
