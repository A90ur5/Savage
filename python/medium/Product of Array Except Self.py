class Solution:
    #def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        lenN = len(nums)
        left_right_product = [1] * lenN
        right_left_product = [1] * lenN
        left_right_product[0] = nums[0]
        right_left_product[lenN-1] = nums[lenN-1]
        for i in range(1, lenN-1):
            left_right_product[i] = nums[i] * left_right_product[i-1]
            right_left_product[lenN-i-1] = nums[lenN-i-1] * right_left_product[lenN-i]

        #print(left_right_product)
        #print(right_left_product)

        res = [0] * lenN
        res[0] = right_left_product[1]
        res[lenN-1] = left_right_product[lenN-2]
        for i in range(1, lenN-1):
            res[i] = left_right_product[i-1] * right_left_product[i+1]

        return res

if __name__ == '__main__':
    ans = Solution()
    testData = [-1,1,0,-3,3]
    print(ans.productExceptSelf(testData))
