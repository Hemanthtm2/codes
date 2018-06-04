#!/usr/bin/python 
import math
def printLog(x):

  if x < 1:
     print "logarithm is only for +ve integers\n"
     return
  
  result=math.log(x)
  print "Logarithm of",x,"is",result

en=int(raw_input("Enter the value for finding logarithm\n"))

printLog(en)
