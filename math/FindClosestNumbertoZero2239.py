# 7ms beats 44%

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lis = []
        i = 0
        leng = len(nums)
        cur_p = 1000000000
        cur_n = -1000000000
        while i < leng:
            if nums[i] > 0 and nums[i] < cur_p:
                cur_p = nums[i]
            elif nums[i] < 0 and nums[i] > cur_n:
                cur_n = nums[i]
            elif nums[i] == 0:
                return 0
            i += 1
        if cur_p > cur_n * -1:
            return cur_n
        elif cur_p <= cur_n * -1:
            return cur_p

# better solution
# beats 85%

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lowest = nums[0]
        for i in nums:
            if abs(i) < abs(lowest):
                lowest = i
        if lowest < 0 and abs(lowest) in nums:
            return abs(lowest)
        else:
            return lowest