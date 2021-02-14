#! /usr/bin/python
try:
    fo = open("foo3.txt","r")
    print fo.readline()

except IOError:
    print "error in reading the file"

else:
    print "read successfully"
    fo.close()
