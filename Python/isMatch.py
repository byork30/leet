class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ip = 0
        i = 0
        isMatch = True
        while i < len(s):
            if ip >= len(p):
                break
            letter = s[i]
            if not (p[ip] == '.' or p[ip] == '*'):
                isMatch = (letter == p[ip])
                ip += 1
            elif p[ip] == '.':
                ip += 1
            else:
                if s[i-1] == '.':
                    
                
        return isMatch
