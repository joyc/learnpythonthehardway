# -*- coding: utf-8 -*-
from sys import argv
script, filename = argv

txt = open(filename)

print "The %r content is: " % filename
print txt.read()
txt.close()
