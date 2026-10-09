class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        palindrome = s[0]
        if s[0] == s[1]:
            palindrome = s[0:2]
        i = 1
        while i < len(s) - 1:
            tempPalindrome = ""
            if s[i-1] == s[i+1]:
                tempPalindrome = self.pal(s, i-1, i+1)
            if s[i] == s[i + 1]:
                evenPalindrome = self.pal(s, i, i+1)
                if len(evenPalindrome) > len(tempPalindrome):
                    tempPalindrome = evenPalindrome
            if len(tempPalindrome) > len(palindrome):
                palindrome = tempPalindrome
            i += 1
        return palindrome
    
    def pal(self, s, j, k):
        while j > 0 and k < len(s) - 1 and s[j-1] == s[k+1]:
            j -= 1
            k += 1
        return s[j:k+1]
