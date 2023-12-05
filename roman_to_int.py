#!/usr/bin/env python3

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        subtractors = ("I","X","C")

        result = 0
        prev = ""
        
        for letter in s:
            result += numerals[letter]
            if ((prev in subtractors) and (numerals[letter]-numerals[prev])>0):
                result -= 2*numerals[prev]
            prev = letter

        return result

roman="MCMXCII"

translator=Solution()
latin=translator.romanToInt(roman)

print(f'{roman} means {latin}')
