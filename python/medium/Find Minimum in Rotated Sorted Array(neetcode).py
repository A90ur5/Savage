class Solution:
    #def findMin(self, nums: List[int]) -> int:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (r + l) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res

'''
It also can works
        while l < r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (r + l) // 2
            if nums[m] >= nums[l]:
                l = m + 1
                res = min(nums[l], res)
            else:
                r = m - 1
                res = min(nums[m], res)

        return res
'''


if __name__ == '__main__':
    ans = Solution()
    testData = [2, 3,4,5,1]
    print(ans.findMin(testData))