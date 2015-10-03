#
# This program converts a number to roman numeral.
#

num = float(input("Enter a number between 1 and 10: "))

# These if statements converts number to roman numeral.
if num == 1:
    print(int(num), ": I")
elif num == 2:
    print(int(num), ": II")
elif num == 3:
    print(int(num), ": III")
elif num == 4:
    print(int(num), ": IV")
elif num == 5:
    print(int(num), ": V")
elif num == 6:
    print(int(num), ": VI")
elif num == 7:
    print(int(num), ": VII")
elif num == 8:
    print(int(num), ": VIII")
elif num == 9:
    print(int(num), ": IX")
elif num == 10:
    print(int(num), ": X")
    
# This if statement produces an error when user
# inputs a greater or lesser value from 1-10
elif num < 0 or num > 10:
    print('ERROR! Invalid number: not between 1 and 10.')

# This if statement produces an error when user
# inputs any decimal value
else:
    print('ERROR! Fractions are not allowed!')

   