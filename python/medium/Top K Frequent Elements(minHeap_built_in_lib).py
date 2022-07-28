from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        numsCounter = Counter()
        for num in nums:
            numsCounter[num] += 1

        i = 0
        minHeap = [(0, 0)] * k
        for n, v in numsCounter.items():
            if i < k:
                print(minHeap)
                minHeap[i] = (v, n)
                i += 1
            else:
                if i == k:
                    heapify(minHeap)
                    i += 1
                if v > minHeap[0][0]:
                    heappop(minHeap)
                    heappush(minHeap, (v, n))
        
        return [n for v, n in minHeap]


if __name__ == '__main__':
    ans = Solution()
    testData = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
    print(ans.topKFrequent(testData, 3))
