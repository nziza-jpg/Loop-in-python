# python program to check if a number is prime
# take input from the user
num = int(input("Enter a number: "))
# check if number is greater than 1 (since primes are > 1)
if num > 1:
    # loop only up to the square root of num for efficiency
    for i in range(2, int(num**0.5) + 1):
        #if num is divisible by any number, it is not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        # if no divisors were found, the number is prime
    else:
        print(f"{num} is a prime number.")
else:
    # numbers less than 2 are not prime
    print(f"{num} is not a prime number.")
    