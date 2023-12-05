#!/usr/bin/env python3

class Solution:
  def mySqrt(self,x):
    """
    :type x: int
    :rtype: int
    """
    ## Newtons method
    #y0 = x
    #tol=1e-7
    #
    #while (abs(y0*y0-x)>tol):
    #  y1 = y0 -(y0*y0-x) / (2.0*y0)
    #  y0 = y1
    #
    #return abs(y0) 

    # bisection
    a = 0.1
    b = x
    tol = 1e-7

    while (abs(a*a-x)>tol):
      fa = a*a-x
      m = (a+b)/2.0
      fm = m*m-x

      if (fa*fm<0):
        b = m
        continue
      else:
        a = m

    return abs(a)

root = Solution()

x = 2.0
y = root.mySqrt(x)
print(y)

x = 4.0
y = root.mySqrt(x)
print(y)

x = 8.0
y = root.mySqrt(x)
print(y)
