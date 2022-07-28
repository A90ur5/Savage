class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashmap = {}
        for i, value in enumerate(nums):
            myTarget = target - value
            if myTarget in myHashmap:
                return [myHashmap[myTarget], i]
            myHashmap[value] = i