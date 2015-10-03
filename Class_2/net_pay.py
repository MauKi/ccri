name = input('Enter name: ')
hrsWorked = float(input('Hours worked last week: '))
payRate = float(input('Hourly pay rate: '))

grossPay = hrsWorked * payRate
netPay = grossPay * .12
netPay = grossPay - netPay

print(name, "'s Gross Pay: $", format(grossPay,'.2f'), sep = '')
print(name, "'s Net Pay:   $", format(netPay,'.2f'), sep = '')