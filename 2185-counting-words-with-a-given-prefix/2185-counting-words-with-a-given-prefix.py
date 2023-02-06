class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        pref_length = len(pref)
        for word in words:
            if len(word) >= pref_length and word[:pref_length] == pref:
                count += 1
        return count