# Runtime 0ms beats 100%

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        target = 0
        target += nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                target += nums[i]
            else:
                break
        while True:
            if target in nums:
                target += 1
            else:
                return target