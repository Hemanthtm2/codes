#!/usr/bin/python
import string

def findlower(str,ch):
  index=0
  for ch in str:
     if str[index]==ch:
       if ch==string.lowercase:
          return ch
     index=index+1
         

  return -1


print findlower("Hemanth",'e')
