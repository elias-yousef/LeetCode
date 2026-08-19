class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        miin = prices[0]
        for i in prices[1:]:
            if i > miin:
                max_prof = max(max_prof, i - miin)
            else:
                miin = i
        return max_prof