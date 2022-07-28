class Solution:
    #def rob(self, nums: List[int]) -> int:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[0]+nums[2], nums[1])
        dp = {0 : nums[0], 1 : max(nums[0], nums[1]), 2 : max(nums[0]+nums[2], nums[1])}
        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            
        return max(dp[n-1], dp[n-2])
        
        
if __name__ == '__main__':
    ans = Solution()
    testData = [2,7,9,3,1]
    print(ans.rob(testData))