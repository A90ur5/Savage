from math import ceil


class Solution:
    #def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r
        #print(f"L:{l} R:{r}")
        while l <= r:
            hours_needed = 0
            k = (l + r) // 2
            #print(f"L:{l} R:{r} K:{k}")
            for bananas in piles:
                hours_needed += ceil(bananas/k)

            if hours_needed > h:
                l = k + 1
            elif hours_needed <= h:
                res = min(res, k)
                r = k - 1

        return res


if __name__ == '__main__':
    ans = Solution()
    testData = [30,11,23,4,20]
    print(ans.minEatingSpeed(testData, 6))