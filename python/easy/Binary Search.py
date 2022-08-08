class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = ( l + r ) // 2
            # m = (r - l) // 2 + l
            # it's a safe way to write in a language that you have to deal with datatype
            # such like C++
            # because if the nums arrary is extreme long
            # l + r maybe > 2^31 and then overflow
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