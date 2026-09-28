class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        total = 0
        roman = {'V': 5, 'L': 50, 'D': 500, 'M': 1000}
        romanEx = {'I': (1, ['V', 'X']),'X': (10, ['L', 'C']),'C': (100, ['D', 'M'])}
        while i < len(s):
            letter = s[i]
            if letter in roman:
                total += roman[letter]
            else:
                value, lookup = romanEx[letter]
                if ((i+1 < len(s)) and (s[i+1] in lookup)):
                    total -= value
                else:
                    total += value
            i+=1
        return total

test = Solution()
print(test.romanToInt("XIV"))
print(test.romanToInt("MCMXCIV"))
print(test.romanToInt("LVIII"))
print(test.romanToInt("III"))
print(test.romanToInt("MMI"))
print(test.romanToInt("MDCCCLXXXVIII"))