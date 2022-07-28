class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)*2-1
        newS = ['_']*slen
        ii = 0
        for i in range(0, len(newS), 2):
            newS[i] = s[ii]
            ii += 1


        maxlen, curlen = 0, 0
        start, end = 0, 0
        for i in range(slen):
            left, right = i, i
            while left >= 0 and right < slen and newS[left] == newS[right]:
                if newS[left] != '_':
                    curlen = right - left + 1
                    if curlen > maxlen:
                        maxlen = curlen
                        start = left
                        end = right
                right += 1
                left -=1
        res = newS[start:end+1]
        '''
        res = ""        
        for i in range(start, end+1):
            if newS[i] != '_':
                res += newS[i]
        '''
        return ''.join(filter(lambda x : x != '_', res))

if __name__ == '__main__':
    ans = Solution()
    testData = "abb"
    print(ans.longestPalindrome(testData))