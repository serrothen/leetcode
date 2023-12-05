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

      t=s[0]
      idx = 1
      valid = True
      while (valid and idx<length):
        # no closing
        if (s[idx] in op):
          t=s[idx]
          idx+=1
          continue
        
        # non-matching closing encountered
        if ((s[idx] in cl) and (cl_dict[s[idx]]!=t)):
          return False

        # matching closing encountered
        if ((s[idx] in cl) and (cl_dict[s[idx]]==t)):
          s_new = s[:idx-1]+s[idx+1:]
          if (len(s_new)==0): return True
          print(s_new)
          valid=self.isValid(s_new)
          return valid

      # exhausted string
      return False
          
valid = Solution()

s = "()"
print(s)
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "()[]{}"
print(s)
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "(]"
print(s)
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "(([]{}(()))())[]"
print(s)
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")

s = "(((("
print(s)
val=valid.isValid(s)
if (val): print("Valid")
else: print("Invalid")
