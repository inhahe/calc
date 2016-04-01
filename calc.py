from __future__ import division
import sys
from math import *
v = eval(''.join(sys.argv[1:]))
if type(v) is int:
  print "{:,d}".format(v)
elif type(v) is float:
  print "{:,f}".format(v)
else:
  print v


    

