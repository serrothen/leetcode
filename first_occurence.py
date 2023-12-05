class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        lHay = len(haystack)
        lNeedle = len(needle)

        loc = -1
        for ii in range(lHay-lNeedle):
            if (haystack[ii:ii+lNeedle]==needle):
                loc = ii
                break;
        return loc


sol = Solution()

haystack = "sadbutsad"
needle = "sad"
loc = sol.strStr(haystack,needle)
print(loc)

haystack = "leetcode"
needle = "leeto"
loc = sol.strStr(haystack,needle)
print(loc)
