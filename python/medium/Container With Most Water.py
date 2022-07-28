class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer, rightPointer = 0, len(height) - 1
        maxArea = 0
        while leftPointer < rightPointer:
            maxArea = max(maxArea, (rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer]))
            if height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
                
        return maxArea