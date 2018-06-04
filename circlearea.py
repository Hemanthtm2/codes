#1/usr/bin/python 
import math

def area(radius):

  area=math.pi*radius**2

def distance(x1,y1,x2,y2):

  dx=x2-x1
  dy=y2-y1
  dsquared=dx**2+dy**2
  result=math.sqrt(dsquared)
  return result 



def areacir(xc,yc,xp,yp):

   radius=distance(xc,yc,xp,yp)
   result=math.pi*radius**2
   return result


print areacir(2,4,6,8)



