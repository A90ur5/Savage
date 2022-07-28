class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            '''
            res = n & 1
            if res == 1:
                total += 1
            '''
            total += (n & 1)
            n = n >> 1
        return total