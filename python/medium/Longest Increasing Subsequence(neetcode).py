class Solution:
    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums) -> int:
        lenN = len(nums)
        dp = [0] * lenN
        for i in range(lenN-1, -1, -1):
            maxSeq = 1
            for j in range(i+1, lenN):
                if nums[j] > nums[i]:
                    maxSeq = max(dp[j]+1, maxSeq)
            dp[i] = maxSeq
        return max(dp)
        
if __name__ == '__main__':
    ans = Solution()
    testData = [10,9,2,5,3,7,101,18]
    print(ans.lengthOfLIS(testData))
    #print(ans.dp)