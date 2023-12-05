#!/usr/bin/python3

class Solution:
  def climbStairs(self,n):
      """
      :type n: int
      :rtype: int
      """

      if (n==1): return 1

      if (n==2): return self.climbStairs(1)+1

      if (n>2): return self.climbStairs(n-1)+self.climbStairs(n-2)


walk = Solution()


for ii in range(1,11):
  poss = walk.climbStairs(ii)
  print(f'{ii}: {poss}')
