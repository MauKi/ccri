#
# This program displays user's letter grade
#
score = float(input('What is your test score? '))
#
# This statement converts test score to grade
if score >= 90 and score <= 100:
    print('You got an A!')
elif score >= 80 and score <= 89.99:
    print('You got a B!')
elif score >= 70 and score <= 79.99:
    print('You got a C!')
elif score >= 60 and score <= 69.99:
    print('You got a D!')
else:
    print('You got an F!')