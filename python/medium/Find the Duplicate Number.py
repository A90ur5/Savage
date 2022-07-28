class Solution:
    #def findDuplicate(self, nums: List[int]) -> int:
    def findDuplicate(self, nums) -> int:
        #always inbound
        '''
        if len(nums) < 2:
            return ''
        elif len(nums) == 2:
            return nums[0]
        '''

        slowPtr, fastPtr = 0, 0

        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            #print("slowPtr: " + str(slowPtr) + ", fastPtr: " + str(fastPtr))
            if nums[slowPtr] == nums[fastPtr]:
                break

        slowPtr2 = 0
        '''
        while nums[slowPtr] != nums[slowPtr2]:
            slowPtr = nums[slowPtr]
            slowPtr2 = nums[slowPtr2]

        return nums[slowPtr]
        '''
        while True:
            if slowPtr == slowPtr2:
                return slowPtr
            slowPtr = nums[slowPtr]
            slowPtr2 = nums[slowPtr2]
        




if __name__ == '__main__':
    ans = Solution()
    testData = [2,5,9,6,9,3,8,9,7,1]
    print(ans.findDuplicate(testData))
