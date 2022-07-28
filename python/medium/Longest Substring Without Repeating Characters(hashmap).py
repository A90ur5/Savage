class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hashmap = {}

        start = 0
        max_length = 0
        i = 0
        length = len(s)

        while i < length:
            if s[i] in hashmap:
                if (i - start) > max_length:
                    max_length = (i - start)
                start = hashmap[s[i]] + 1
                i = start
                hashmap.clear()

            hashmap[s[i]] = i
            i += 1

        if (i - start) > max_length:
            max_length = (i - start)

        return max_length