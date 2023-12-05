class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sgn = 1
        for num in nums:
            if (num==0):
                sgn = 0
                break
            if (num<0):
                sgn*=-1
        
        return sgn
