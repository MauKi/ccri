#
# This instruction will open an input file called testfile.txt
infile = open('testfile.txt','r')
#
# This instruction reads a line from the file and puts it into
value = float(infile.readline())
#
# This instruction closes the input file
infile.close()