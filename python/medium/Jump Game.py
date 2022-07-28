class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums)-1
        if destination == 0:
            return True
        
        curr_pos = 0
        maxPos = (0, 0)
        i = 0

        while i < destination:
            nextPosCandidate = i + nums[i]
            if i > curr_pos + nums[curr_pos]:
                if maxPos[1] < i:
                    return False
                curr_pos = maxPos[0]
                maxPos = (0, 0)

            if nextPosCandidate >= destination:
                return True
            elif nextPosCandidate > maxPos[1]:
                maxPos = (i,  nextPosCandidate)

            i += 1
        
        return False