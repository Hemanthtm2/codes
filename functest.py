#!/usr/bin/python 



def printTwice(test):
   print test,test


def catT(ch1,ch2):
  ch=ch1+ch2
  printTwice(ch)


print "print two times test",printTwice(10)
print "A function call another function example",catT('Hemanth','Varada')


