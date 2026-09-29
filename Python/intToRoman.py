class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        place = 0
        sub = (("IV", "IX"), ("XL", "XC"), ("CD", "CM"))
        lookup = (('I', 'V'), ('X', 'L'), ('C', 'D'))
        while place < 3:
            tempStr = ""
            rem = num % 10
            num //= 10
            if rem % 5 == 4:
                tempStr = sub[place][int(rem > 5)]
            else:
                tempStr = lookup[place][1] * int(rem >= 5) + lookup[place][0] * (rem % 5)
            roman = tempStr + roman
            place += 1
        return (num * 'M' + roman)
