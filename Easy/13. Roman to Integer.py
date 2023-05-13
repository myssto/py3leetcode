"""
5/13/23
Runtime: 49 ms
Memory Usage: 16.2 MB
Beats 71.71%
"""

class Solution:
    def __init__(self):
        self.conversions = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:

        nums = [self.conversions[char] for char in s]

        converted = []
        jump = 0
        listlen = len(nums) - 1
        for idx, n1 in enumerate(nums):
            # Check for jump
            if jump:
                jump = 0
                continue
            # Check if last value
            if idx == listlen:
                converted.append(n1)
                continue
            # Check if adding or subtracting
            n2 = nums[idx + 1]
            if n1 >= n2:
                converted.append(n1)
            else:
                # Jump to idx+1 if subtracting
                converted.append(n2-n1)
                jump = 1

        return sum(converted)