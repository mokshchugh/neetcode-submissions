class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str


    def decode(self, s: str) -> List[str]:

        decoded = []
        idx = 0

        while idx < len(s):
            j = 0
            while s[idx+j] != '#':
                j += 1
            word_len = int(s[idx:idx+j])
            word = s[idx + j + 1 : idx + j + 1 + word_len]
            decoded.append(word)
            idx += j + 1 + word_len

        return decoded
