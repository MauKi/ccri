infile = open('f2_number.txt','r')
#
# This instruction reads a line from the file and puts it into
celsius = float(infile.readline())
#
# This instruction closes the input file
infile.close()

farenheit = celsius * (9/5) + 32
print('Celsius:   ', celsius, sep = ' ')
print('Farenheit: ', farenheit, sep = ' ')