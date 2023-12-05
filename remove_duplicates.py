#!/usr/bin/env python3

import random

class Solution:
  def removeDuplicates(self,nums):
      """
      :type nums: List[int]
      :rtype: int
      """

      pos=0
      prev=-1
      length=len(nums)
      for ii in range(length):
        if (nums[ii]!=prev):
           nums[pos]=nums[ii]
           prev=nums[pos]
           pos+=1

      return pos

remover=Solution()

nums=[random.randint(0,100) for ii in range(100)]
nums.sort()

print(nums)

ref=list(set(nums))
print(ref)

rel_len=remover.removeDuplicates(nums)
print(nums)
print(f'Expect: {len(ref)}. Got {rel_len}')

