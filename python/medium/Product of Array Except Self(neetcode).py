class Solution:
    #def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        lenN = len(nums)
        res = [1] * lenN
        prefix = 1
        for i in range(lenN):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(lenN-1 , -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

if __name__ == '__main__':
    ans = Solution()
    testData = [-1,1,0,-3,3]
    print(ans.productExceptSelf(testData))