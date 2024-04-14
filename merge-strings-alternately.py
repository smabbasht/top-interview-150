class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        longer = 1 if len1 > len2 else 2
        n = min(len1, len2)

        word = [0]*(len1+len2)

        word[:n*2:2] = word1[:n]
        word[1:n*2:2] = word2[:n]

        if longer == 1:
            word[n*2:] = word1[n:]
        else:
            word[n*2:] = word2[n:]

        return "".join(word)
