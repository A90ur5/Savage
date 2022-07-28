class Solution:
    #def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums) -> int:
        res = max(nums)
        minRes = maxRes = 1
        for n in nums:
            if n == 0:
                minRes = maxRes = 1
                #The function still work without this if-statement

            tmp = maxRes
            maxRes = max(n * minRes, n * maxRes, n)
            minRes = min(n * minRes, n * tmp, n)
            res = max(maxRes, res)
        return res
        






if __name__ == '__main__':
    ans = Solution()
    testData = [-2,3,-4]
    print(ans.maxProduct(testData))