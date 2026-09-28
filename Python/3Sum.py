class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tups = set()
        for i in range(len(nums)-2):
            repeats = []
            num1 = nums[i]
            for j in range(len(nums) - 1 - i):
                num2 = nums[i+1:][j]
                if num2 in repeats:
                    continue
                num3 = 0 - (num1+num2)
                if num3 in nums[i+1:][j + 1:]:
                    repeats.extend([num2, num3])
                    tups.add(tuple(sorted([num1, num2, num3])))
        out = []
        for tup in tups:
            out.append(list(tup))
        return out

# Currently times out on very large lists
