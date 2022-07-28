class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min = 0
        max = len(nums)
        total = 0
        for num in nums:
            total += num
            
        return (int)(((max + min) * (len(nums) + 1)) / 2 - total)