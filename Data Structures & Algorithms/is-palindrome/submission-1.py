class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [c.lower() for c in s if c.isalnum()]
        s2 = s1[::-1]
        if s1 == s2:
            return True
        return False
        