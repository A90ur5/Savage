class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if i != (offset << 1):
                res[i] = res[i-offset] + 1
            else:
                res[i] = 1
                offset = offset << 1
            
        return res