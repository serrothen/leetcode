class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        val = num
        nsteps = 0

        while (val>0):
            if (val%2==0):
                val //= 2
            else:
                val -=1
            nsteps += 1

        return nsteps
