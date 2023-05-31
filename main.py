# CracklePop program
#
# Requirements: Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3,
# print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print
# CracklePop. You can use any language.

# Loop from 1 through 100
for num in range(1, 101):
    # Check if number is divisible by both 3 and 5, if so print CracklePop
    if num % 3 == 0 and num % 5 == 0:
        print("CracklePop")
    # Otherwise, check if number is divisible by 3, if so print Crackle
    elif num % 3 == 0:
        print("Crackle")
    # Otherwise, check if number is divisible by 5, if so print Pop instead
    elif num % 5 == 0:
        print("Pop")
    # If none of the above apply, then simply print number
    else:
        print(num)
