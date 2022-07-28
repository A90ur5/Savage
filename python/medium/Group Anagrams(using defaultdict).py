from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            str_ascii = [0]*26

            for c in str:
                char_ascii = ord(c) - ord('a')
                str_ascii[char_ascii] += 1
            

            res[tuple(str_ascii)].append(str)

        return res.values()