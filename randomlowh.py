#!/usr/bin/python 

import random

def randomn(low,high):

  if low < high:
    for i in range(low,high):
       x=random.random()
       print x

randomn(1,20)
