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
        print(numsCounter)
        maxHeap = [(0,0)] * (len(numsCounter) + 1)
        i = 1
        for n, v in numsCounter.items():
            if i == 1:
                maxHeap[1] = (n, v)
                i += 1
            else:
                #insert n, v to min heap
                maxHeap[i] = (n, v)
                j = i
                #compare left and right
                if i % 2 == 1 and maxHeap[i][1] > maxHeap[i-1][1]:
                    # i is even -> left child
                    # i is odd -> right child
                    #if right child > left child than swap
                    tmp = maxHeap[i]
                    maxHeap[i] = maxHeap[i-1]
                    maxHeap[i-1] = tmp

                while(maxHeap[j][1] > maxHeap[j >> 1][1] and j > 1):
                    #if child > parents than swap
                    tmp = maxHeap[j]
                    maxHeap[j] = maxHeap[j >> 1]
                    maxHeap[j >> 1] = tmp
                    j = j >> 1

                
                if j > 2 and j % 2 == 1 and maxHeap[j][1] > maxHeap[j-1][1]:
                    #if right child > left child than swap
                    tmp = maxHeap[j]
                    maxHeap[j] = maxHeap[j-1]
                    maxHeap[j-1] = tmp

                i += 1
        print(maxHeap)
        res = [0]*k
        for i in range(k):
            res[i] = maxHeap[i+1][0]

        return res


if __name__ == '__main__':
    ans = Solution()
    testData = [4,1,-1,2,-1,2,3]
    print(ans.topKFrequent(testData, 2))
