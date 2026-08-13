class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        left = 0
        right = 0

        char_set = set()

        while right < len(s):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            length = right - left + 1
            right += 1
            max_length = max(max_length, length)

        return max_length
