import math
class Solution:
    #def findMin(self, nums: List[int]) -> int:
    def findMin(self, nums):
        i = 1
        rEdge = len(nums)-1
        if rEdge == 0:
            return nums[0]
        lEdge = 1
        while True:
            while nums[i] > nums[0]:
                #go right
                if lEdge == rEdge:
                    return nums[0]
                lEdge = i
                i = math.ceil((i + rEdge) / 2)
                #print("i:" + str(i) + " rEdge: " + str(rEdge))
            
            while nums[i] < nums[0]:
                if nums[i-1] < nums[i] and nums[i+1] > nums[i]:
                    #go left                
                    rEdge = i
                    i = math.ceil((i + lEdge) / 2)
                else:
                    #nums[i-1] > nums[i] and nums[i+1] > nums[i]
                    return nums[i]
    
if __name__ == '__main__':
    ans = Solution()
    testData = [2, 3,4,5,1]
    print(ans.findMin(testData))

                
                    
                


