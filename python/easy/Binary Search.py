class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = ( l + r ) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


if __name__ == '__main__':
    ans = Solution()
    testData =[-1,0,3,5,9,12]
    print(ans.search(testData, 9))