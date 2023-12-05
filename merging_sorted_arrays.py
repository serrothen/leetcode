#!/usr/bin/env python3

class Solution:
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None. Do not return anything, modify nums1 in-place instead.
    """

    shifts = []

    # check before first entry of nums1
    pos1 = 0
    pos2 = 0
    for ii in range(n):
      if (nums2[ii]<nums1[pos1]): pos2+=1
    shifts.append(pos2)

    # check intervals in num1
    for ii in range(1,m):
      pos1 = ii
      pos2 = 0
      for jj in range(n):
        if (nums2[jj]>=nums1[pos1-1] and nums2[jj]<nums1[pos1]): pos2+=1
      shifts.append(pos2)

    # check after last entry of nums1
    pos1 = m-1
    pos2 = 0
    for ii in range(n):
      if (nums2[ii]>=nums1[pos1]): pos2+=1
    shifts.append(pos2)

    # assemble
    rhs1=len(nums1)
    rhs2=n
    for ii in range(m,0,-1):
        nums1[rhs1-shifts[ii]:rhs1] = nums2[rhs2-shifts[ii]:rhs2]
        rhs1 -= shifts[ii]
        rhs2 -= shifts[ii]
        nums1[rhs1-1] = nums1[ii-1]
        rhs1 -= 1
    nums1[rhs1-shifts[0]-1:rhs1] = nums2[rhs2-shifts[0]-1:rhs2]


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merger = Solution()
merger.merge(nums1,m,nums2,n)
print(nums1)


nums1 = [1]
m = 1
nums2 = []
n = 0

merger = Solution()
merger.merge(nums1,m,nums2,n)
print(nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1

merger = Solution()
merger.merge(nums1,m,nums2,n)
print(nums1)


nums1 = [1,1,2,3,5,8,13,0,0,0,0,0]
m = 7
nums2 = [1,3,5,7,9]
n = 5

merger = Solution()
merger.merge(nums1,m,nums2,n)
print(nums1)
