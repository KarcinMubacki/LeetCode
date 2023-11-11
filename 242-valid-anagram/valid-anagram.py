class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True