class Solution:
    def countSubstrings(self, s: str) -> int:
        lenS = len(s)
        counter = 0
        for i in range(lenS):
            #odd
            l, r = i, i
            while l >= 0 and r < lenS and s[l] == s[r]:
                l -= 1
                r += 1

                counter += 1


            #even
            l, r = i, i+1
            while l >= 0 and r < lenS and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 1

        return counter


if __name__ == '__main__':
    ans = Solution()
    testData = "aaa"
    print(ans.countSubstrings(testData))