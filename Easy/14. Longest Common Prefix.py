"""
5/13/23
Runtime: 225 ms
Memory Usage: 16.6 MB
Beats 5.56%
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Check if any matching first letter
        if not len(strs):
            return ''
        if len(strs) == 1:
            return strs[0]
        if False in [len(word) for word in strs]:
            return ''

        def allmatch(seq):
            match = 1
            for idx, l1 in enumerate(seq):
                for idy, l2 in enumerate(seq):
                    if idx == idy:
                        continue
                    if l1 != l2:
                        match = 0
                        break
            return match

        ini = [word[0] for word in strs]
        if not allmatch(ini):
            return ''

        def loop(seq, prefix):
            x = [word[len(prefix)] for word in seq if len(prefix) < len(word)]
            if not len(x) < len(seq) and allmatch(x):
                return loop(seq, prefix + x[0])
            else:
                return prefix

        return loop(strs, ini[0])