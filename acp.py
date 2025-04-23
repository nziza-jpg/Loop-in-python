# Get input from user
num = input("Enter a number to check if it's an Armstrong number: ")
# Calculate the number of digits
num_of_digits = len(num)
# Calculate sum of each digit raised to the power of number of digits
sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit) ** num_of_digits
# Checking if Armstrong
if sum_of_digits == int(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")