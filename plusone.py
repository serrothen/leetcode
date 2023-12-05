#!/usr/bin/env python3

class Solution:
  def plusOne(self,digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    length = len(digits)
    x=1
    for ii in range(length-1,-1,-1):
      y = digits[ii]+x
      if (y<10):
         digits[ii]=y
         break
      else:
         x = int(float(y)/10.0)
         rest = int(y%10)
         digits[ii]=rest
         if (ii==0):
            digits_copy = digits
            digits = [1]
            digits.extend(digits_copy[:])


    return digits

addOne = Solution()

num1 = [3,1,4,1,5,9,2,6,5,4]
num2 = addOne.plusOne(num1)
print(num2)

num1 = [3,1,4,1,5,9,2,6,5,9]
num2 = addOne.plusOne(num1)
print(num2)

num1 = [9,9,9,9,9]
num2 = addOne.plusOne(num1)
print(num2)
