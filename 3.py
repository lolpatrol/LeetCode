# https://leetcode.com/submissions/detail/230421552/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = len(set(list(s)))
        st = s
        left = 0
        longest = 0
        current = ""
        while left < len(st):
            if longest == max_length:
                return longest
            current += st[left]
            if len(set(current)) == len(current):
                if len(current) > longest:
                    longest = len(current)
                left += 1
            else:
                index = st.index(current[-1])
                st = st[index+1:]
                current = ""
                left = 0
        return longest

