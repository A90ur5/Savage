from collections import defaultdict
from itertools import count

class Solution:
    def zero(self):
        return 0

    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        numsCounter = defaultdict(self.zero)
        for num in nums:
            numsCounter[num] += 1
        counterList = [(n, v) for n, v in numsCounter.items()]
        counterList.sort(reverse=True ,key = lambda x : x[1])

        res = []
        for i in range(k):
            res.append(counterList[i][0])

        return res

if __name__ == '__main__':
    ans = Solution()
    testData = [1,1,1,2,2,3]
    print(ans.topKFrequent(testData, 2))
