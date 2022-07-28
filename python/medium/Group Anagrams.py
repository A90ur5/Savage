class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            str_ascii = [0]*26

            for c in str:
                char_ascii = ord(c) - ord('a')
                str_ascii[char_ascii] += 1
            str_ascii_tuple = tuple(str_ascii)

            if str_ascii_tuple in res:
                res[str_ascii_tuple].append(str)
            else:
                res[str_ascii_tuple] = [str]

        return res.values()