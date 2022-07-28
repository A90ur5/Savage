class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if len(s) != len(t):
            return False
        '''
        dict_s = {}
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1

        for c in t:
            if c in dict_s:
                if dict_s.get(c) == 1:
                    del dict_s[c]
                else:
                    dict_s[c] -= 1                
            else:
                return False
        #return True

        if dict_s.keys():
            return False
        return True

'''
solution with python built-in function

1.
    return Counter(s) == Counter(t)
    // time: O(n)    space: O(n)
    // same as code below
2.
    return sorted(s) == sorted(t)
    // time: O(nlogn)    space: O(1)
'''