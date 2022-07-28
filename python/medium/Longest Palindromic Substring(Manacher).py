class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        # 在所有字符中间插入#
        def transform(s):
            return '$#' + '#'.join(list(s)) + '#&'
        
        if s == '':
            return s
        # 初始化
        s = transform(s)
        p = [0 for _ in range(len(s)+1)]
        mr, id_ = 0, 0
        # 首尾是特殊字符，所以下标从1到len(s)-2
        for i in range(1, len(s)-1):
            # 计算p[i]
            p[i] = 1 if mr <= i else min(p[2*id_-i], mr - i)

            # 只有当前i已经摆脱id限制，或者是第三种情况时，才有可能继续延伸
            # 这个只是优化，不加这个判断一样可以运行
            if mr <= i or p[2*id_-i] == mr - i:
                while s[i - p[i]] == s[i + p[i]]:
                    p[i] += 1

                if i + p[i] > mr:
                    mr, id_ = i + p[i], i
        # 找到长度最长的下标
        id_ = p.index(max(p))
        # 获得整个回文的字符串
        palindromic = s[id_ - p[id_]+1: id_ + p[id_]]
        # 过滤掉#，还原为原字符
        return ''.join(filter(lambda x: x != '#', list(palindromic)))