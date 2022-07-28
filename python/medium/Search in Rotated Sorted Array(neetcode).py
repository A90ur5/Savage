# Binary Search directly without finding pivot
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,  right = 0, len(nums)-1
        mid = right // 2

        while left <= right:
            if target == nums[mid]:
                return mid
            
            elif target < nums[left]:
                #target is in rotated portion
                if nums[mid] < nums[left]:
                    #mid and target are in the same portion
                    if target < nums[mid]:
                        #go left
                        right = mid - 1
                        mid = (left + right) // 2

                    elif target > nums[mid]:
                        #go right
                        left = mid + 1
                        mid = (left + right) // 2

                elif nums[mid] >= nums[left]:
                    #mid and target are in different portion
                    #from left to right: left -> mid -> pivot -> target
                    #go right
                    left = mid + 1
                    mid = (left + right) // 2
            
            elif target >= nums[left]:
                #target is in normal portion
                if nums[mid] >= nums[left]:
                    #mid and target are in same portion
                    if target < nums[mid]:
                        #go left
                        right = mid - 1
                        mid = (left + right) // 2
                    elif target > nums[mid]:
                        #go right
                        left = mid + 1
                        mid = (left + right) // 2

                elif nums[mid] < nums[left]:
                    #mid and target are in different portion
                    #form left to right: left -> target -> pivot -> mid
                    #go left
                    right = mid - 1
                    mid = (left + right) // 2

        return -1