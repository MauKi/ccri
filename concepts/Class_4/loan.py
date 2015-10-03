#
# This program tests is user qualifies for loan
#
salary = float(input('Annual Income: '))
years = float(input('Years worked:   '))

# Minimum qualifications
minSalary = 30000
minYears = 2

# This program determines if user qualifies.
if salary >= minSalary and years >= minYears:
    print('You are eligible for a loan.')
elif salary < minSalary:
    print('Your salary is too low.')
elif years < minYears:
    print('You haven\'t worked long enough.')