#!/usr/bin/python3

class Solution:
  def isValid(self,s):
      """
      :type s: str
      :rtype: bool
      """

      length = len(s)
      if (length%2!=0):
         return False

      op=("(","[","{")
      cl=(")","]","}")

      cl_dict = {")":"(","]":"[","}":"{"}

      idx=0
      hist = [s[idx]]
      for ii in range(1,length):
        if (s[ii] in op):
           hist.append(s[ii])
           idx += 1
           continue
        if ((s[ii] in cl) and (cl_dict[s[ii]]!=hist[idx])):
          return False
        if ((s[ii] in cl) and (cl_dict[s[ii]]==hist[idx])):
          hist.pop(-1)
          idx-=1
      if (len(hist)==0): return True
          
valid = Solution()

s = "()"
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "()[]{}"
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "(]"
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "(([]{}(()))())[]"
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")
