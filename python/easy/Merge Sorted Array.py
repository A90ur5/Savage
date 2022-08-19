class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        i ,j = m-1, n-1
        for k in range(m+n-1, -1, -1):
            if i < 0:
                nums1[:j+1] = nums2[:j+1]
                break
            
            elif j < 0:
                break

            else:
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1