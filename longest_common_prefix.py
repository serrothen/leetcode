#!/usr/bin/env python3

class Solution:
  def longestCommonPrefix(self,strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      
      length=len(strs)

      # find shortest word
      idx=length
      wl=200
      for ii in range(length):
        li = len(strs[ii])
        if (li<wl):
           wl=li
           idx=ii
      ref=strs[idx]

      for ii in range(length):
        for jj in range(wl,-1,-1):
          if (strs[ii][:jj]==ref[:jj]):
             wl=jj
             break
          if (jj==0):
             wl=0

      return ref[:wl]

measure=Solution()

strs = ["flower","flow","flight"]
prefix=measure.longestCommonPrefix(strs)
print(prefix)

strs = ["lemon","lemmings","lemke"]
prefix=measure.longestCommonPrefix(strs)
print(prefix)

strs = ["dog","racecar","car"]
prefix=measure.longestCommonPrefix(strs)
print(prefix)
