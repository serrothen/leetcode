#!/usr/bin/python3

class Solution:
  def twoSum(self,nums, target):
      """
      :type nums: List[int]
      :type traget: int
      :rtype: List[int]
      """

      length=len(nums)
      success=False

      for ii in range(length):
        if (success): break
        for jj in range(ii+1,length):
          if (nums[ii]+nums[jj]==target):
            print(f'{nums[ii]}+{nums[jj]}={target}')
            loc=[ii,jj]
            break
      return loc

finder=Solution()

nums = [2,7,11,15]
target = 9
loc=finder.twoSum(nums,target)
print(loc)

nums = [3,2,4]
target = 6
loc=finder.twoSum(nums,target)
print(loc)

nums = [3,3]
target = 6
loc=finder.twoSum(nums,target)
print(loc)
