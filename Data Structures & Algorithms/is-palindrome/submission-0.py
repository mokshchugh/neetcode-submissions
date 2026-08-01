class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_stripped = "".join(c.lower() for c in s if c.isalnum())
        high = len(s_stripped) - 1
        low = 0

        while low < high:

            if s_stripped[low] != s_stripped[high]:
                return False

            low += 1
            high -= 1
        
        return True