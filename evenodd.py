#!/usr/bin/python 


def sequence(n):

  while n!=1:
    print n 
    if n%2==0: #n is even
      n=n/2
    else:      #n is odd
     n=n*3+1


val=int(raw_input("Enter the value of n\n"))


sequence(val)


