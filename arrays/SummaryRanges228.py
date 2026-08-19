# 0ms Beats 100%

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        awns = []
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] != nums[i] + 1:
                if nums[i] == start:
                    awns.append(f"{nums[i]}")
                else:
                    awns.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
            i += 1
        if start == nums[-1]:
            awns.append(f"{nums[-1]}")
        else:
            awns.append(f"{start}->{nums[-1]}")
        return awns