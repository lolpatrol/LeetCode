# https://leetcode.com/submissions/detail/231560153/

class Solution:
    pairs = dict()
    def isMatch(self, s: str, p: str) -> bool:
        if(s, p) in self.pairs:
            return self.pairs[(s, p)]
        if not p:
            return not s
        if p[-1] == "*":
            if self.isMatch(s, p[:-2]):
                self.pairs[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == ".") and self.isMatch(s[:-1], p):
                self.pairs[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == ".") and self.isMatch(s[:-1], p[:-1]):
            self.pairs[(s, p)] = True
            return True
        self.pairs[(s, p)] = False
        return False

