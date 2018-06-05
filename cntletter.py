#!/usr/bin/python 

def countLetters(str,ch):

 count=0
 for ch in str:
   if ch=='a':
      count=count+1

 print count

countLetters("Banana",'a')
