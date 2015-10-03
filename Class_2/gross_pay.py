name = input('Enter name: ')
hrsWorked = float(input('Hours worked last week: '))
payRate = float(input('Hourly pay rate: '))
grossPay = hrsWorked * payRate
print(name, ', you made $', format(grossPay,'.2f'), sep = '')