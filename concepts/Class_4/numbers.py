#
# This program displays a message according to user's input of numbers
#
num1 = float(input('Enter first number:  '))
num2 = float(input('Enter second number: '))
#
# This statement compares numbers.
if num1 == num2:
    print('Both numbers are equal!')
elif num1 < num2:
    print(num1, 'is the lowest of the two numbers.')
else:
    print(num2, 'is the highest than the two numbers.')