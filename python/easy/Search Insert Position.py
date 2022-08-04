class Solution:
    #def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        if nums[m] < target:
            return m + 1
        else:
            return m






if __name__ == '__main__':
    ans = Solution()
    testData = [1,3,5,6]
    print(ans.searchInsert(testData,7))