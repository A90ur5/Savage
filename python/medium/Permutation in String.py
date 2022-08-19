class Solution:
    #def checkInclusion(self, s1: str, s2: str) -> bool:
    def checkInclusion(self, s1, s2):
        s1_counter = [0]*26
        s2_counter = [0]*26
        for c in s1:
            s1_counter[ord(c) - ord('a')] += 1
        
        s1_hash = hash(tuple(s1_counter))
        l, r = 0, 0
        for c in s2:
            if r - l < len(s1)-1:
                s2_counter[ord(c) - ord('a')] += 1
                r += 1
            else:
                s2_counter[ord(c) - ord('a')] += 1
                s2_hash = hash(tuple(s2_counter))
                if s1_hash == s2_hash:
                    return True
                else:
                    s2_counter[ord(s2[l]) - ord('a')] -= 1
                    l += 1
                    r += 1
        return False


if __name__ == '__main__':
    ans = Solution()
    testData = "a"
    print(ans.checkInclusion("a", "eidboaoo"))