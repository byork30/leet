class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        positive = True
        if x < 0:
            positive = False
            x *= -1
        while x > 0:
            rev *= 10
            rev += x % 10
            x //= 10
        if not positive:
            rev *= -1
        return rev if rev >= -2**31 and rev <= 2**31 - 1 else 0
