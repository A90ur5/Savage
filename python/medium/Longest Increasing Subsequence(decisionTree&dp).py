from collections import defaultdict

class Solution:
    global dp
    def zero(self):
        return 0

    def dfs(self, i ,nums):
        if self.dp[i] > 0:
            return self.dp[i]
        else:
            maxSeq = set()
            maxSeq.add(1)
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maxSeq.add(self.dfs(j, nums)+1)
            self.dp[i] = max(maxSeq)
            return self.dp[i]



    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums) -> int:
        self.dp = defaultdict(self.zero)
        lenN = len(nums)
        maxSeq = [1] * lenN
        for i in range(lenN):
            maxSeq[i] = self.dfs(i, nums)
        return max(maxSeq)
        
if __name__ == '__main__':
    ans = Solution()
    testData = [7,7,7,7,7,7,7]
    print(ans.lengthOfLIS(testData))
    print(ans.dp)