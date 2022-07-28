class Solution:
    #def rob(self, nums: List[int]) -> int:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0
        n = len(nums)

        #[rob1, rob2, n, n+1, n+2, ...]
        for v in nums:
            temp = max(rob1 + v, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
        
        
if __name__ == '__main__':
    ans = Solution()
    testData = [2,7,9,3,1]
    print(ans.rob(testData))