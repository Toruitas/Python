__author__ = 'Stuart'
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# with open(to_file) as to_file: to_file.write(with open(from_file.read()))
open(to_file,'w').write((open(from_file).read()))

#print("Copying file from {} to {}".format(from_file,to_file))

# we could do these two on one line, too. How?
#in_file = open(from_file)
#indata = in_file.read()

# indata = open(from_file).read()

#print("The input file is {} bytes long".format(len(indata)))
#print("Does the output file exist? {}".format(exists(to_file)))
#print("Ready, hit ENTER to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file,'w')
#out_file.write(indata)
#open(to_file,'w').write(indata)

print("Alright, all done.")
#out_file.close()
#in_file.close()