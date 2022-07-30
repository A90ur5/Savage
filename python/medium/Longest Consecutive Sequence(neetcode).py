class Solution:
    #def longestConsecutive(self, nums: List[int]) -> int:
    def longestConsecutive(self, nums):
        numset = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                res = max(res, length)

        return res

if __name__ == '__main__':
    ans = Solution()
    testData = [0,3,7,2,5,8,4,6,0,1]
    print(ans.longestConsecutive(testData))