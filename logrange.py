#!/usr/bin/python 

import math

def printMlog(n):
  if n < 0:
    print "Loagrithm is only for +ve integers"
    return -1
  elif not isinstance(n,int):
    print "Logarithm is for integers"
  else:
    print math.log(n)


printMlog(10)
