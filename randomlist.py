#!/usr/bin/python 

import random
def randomList(n):
  s=[0]*n
  for i in range(n):
     s[i]=random.random()
  return s


def inBucket(t,low,high):

  count=0
  for num in t:
   if low < num <high:
      count=count+1
  return count 


print randomList(8)


