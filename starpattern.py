# python program to print a star pattern based on the number of rows specified by the user
# get number of rows from user
n = int(input("Enter the number of rows: "))
# outer loop for each row
for i in range(1, n+1):
    # inner loop for each column in the row
    for j in range(i):
        # print star, end with space instead of new line
        print('*', end=' ')
        # after each row, print a new line
    print()