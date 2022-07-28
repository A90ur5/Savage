from collections import defaultdict

class Solution:
    def zero(self):
        return 0

    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        numsCounter = defaultdict(self.zero)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            numsCounter[num] += 1

        for n, v in numsCounter.items():
            freq[v].append(n)

        res = []
        counter = 0
        
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                counter += 1
                if counter == k:
                    return res


if __name__ == '__main__':
    ans = Solution()
    testData = [3,0,1,0]
    print(ans.topKFrequent(testData, 1))
