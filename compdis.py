#!/usr/bin/python 

def compare(x,y):

  if x < y:
    print x, "is less than",y
  elif x > y:
    print x,"is greater than",y
  else:
    print x,"and",y,"are equal"


print compare(2,3)
