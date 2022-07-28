class Solution:
    def robhouse1(self, nums) -> int:
        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n+1, n+2, ...]
        for v in nums:
            temp = max(rob1 + v, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    #def rob(self, nums: List[int]) -> int:
    def rob(self, nums) -> int:
        #neetcode solution
        return max(nums[0], self.robhouse1(nums[1:]), self.robhouse1(nums[:-1]))
        #since rob1 and rob2 are initailize by 0,
        #if I pass an empty list to robhouse1 function,
        #it will just return 0.

        '''
        #my solution
        houseNum = len(nums)
        if houseNum == 1:
            return nums[0]
        elif houseNum == 2:
            return max(nums[0], nums[1])
        elif houseNum == 3:
            return max(nums[0], nums[1], nums[2])
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
        '''


if __name__ == '__main__':
    ans = Solution()
    testData = [200,3,140,20,10]
    print(ans.rob(testData))
    testData = [1,2,1,1]
    print(ans.rob(testData))