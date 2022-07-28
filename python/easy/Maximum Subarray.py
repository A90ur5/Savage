class Solution:
    def maxSubArray(self, nums):
        max = float('-inf')
        local_total = 0
        local_head = 0

        for index in range(len(nums)):
            val = nums[index]
            local_total += val
            if local_total < 0:
                if local_head == index:
                    if val > max:
                        max = val
                else:
                    local_total -= val
                    if local_total > max:
                        max = local_total
                local_head = index + 1
                local_total = 0

            else:
                if local_total > max:
                    max = local_total

        return max

def main():
    mySol = Solution
    #a = mySol.maxSubArray(mySol, [-2,1,-3,4,-1,2,1,-5,4])
    a = mySol.maxSubArray(mySol, [-2, -1])
    print(a)

if __name__ == '__main__':
     main()