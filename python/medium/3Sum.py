class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        lenNums = len(nums)
        res = []
        
        for idx, val in enumerate(sortedNums):
            if val == sortedNums[idx-1] and idx > 0:
                continue
            leftPointer = idx + 1
            rightPointer = lenNums - 1
            while leftPointer < rightPointer:
                threeSum = sortedNums[leftPointer] + sortedNums[rightPointer] + val
                if threeSum > 0:
                    rightPointer -= 1
                
                elif threeSum < 0:
                    leftPointer += 1
                    
                else:
                    res.append([val, sortedNums[leftPointer], sortedNums[rightPointer]])
                    leftPointer += 1
                    while sortedNums[leftPointer] == sortedNums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        
        return res